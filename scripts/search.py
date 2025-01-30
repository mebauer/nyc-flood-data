import pandas as pd
import os
import time
import requests
from datetime import datetime
from sodapy import Socrata

# Source domain for NYC Open Data on Socrata
socrata_token = os.environ.get("SODAPY_APPTOKEN")
socrata_domain = 'data.cityofnewyork.us'

# Initialize Socrata object to fetch data
client = Socrata(
    domain=socrata_domain,
    app_token=socrata_token,
    timeout=1000
)

# Log and output files
export_log = "logs/log.txt"
output_csv = "results/results.csv"

# Function to log dataset-column processing with a timestamp
def log_message(message: str) -> None:
    """Log messages with timestamp."""
    with open(export_log, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{message}\n")

# Function to process small datasets (less than 1 million rows)
def process_small_dataset(id_code: str) -> bool:
    """Process datasets with fewer than 1 million rows."""
    try:
        dataset_url = f"https://data.cityofnewyork.us/api/views/{id_code}/rows.csv?accessType=DOWNLOAD"
        results_df = pd.read_csv(dataset_url)

        if results_df.empty:
            print(f"No data available for {id_code}. Skipping.")
            log_message(f"Skipping {id_code} due to no data.")
            return False
        
        # Filter the dataframe to only include string columns (skip booleans)
        results_df = results_df.select_dtypes(include=['object'])

        for col in results_df.columns:     
            log_message(f"Processing {id_code}, column {col}")

            # Identify rows where column contains 'flood' (case-insensitive)
            contains_flood_ser = (
                results_df
                .loc[results_df[col].astype(str).str.contains('flood', case=False, na=False)][col]
                .value_counts()
            )
               
            if contains_flood_ser.empty:
                print(f"No relevant data in column {col} for {id_code}. Skipping.")
                log_message(f"No relevant data in column {col} for {id_code}. Skipping.")
                continue  # Skip column if no relevant values found

            # Reset index and rename columns
            contains_flood_ser_df = contains_flood_ser.reset_index()
            contains_flood_ser_df.columns = ['value', 'count']

            # Add timestamp, column name, and id_code to the DataFrame
            contains_flood_ser_df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            contains_flood_ser_df['column'] = col
            contains_flood_ser_df['id'] = id_code

            # Append the results to the CSV file
            contains_flood_ser_df.to_csv(output_csv, mode='a', header=False, index=False)
            print(f"Processed {id_code} - {col}")

        return True

    except requests.exceptions.RequestException as e:
        print(f"Request error for id_code {id_code}: {str(e)}")
        log_message(f"Error for {id_code} (RequestException): {str(e)}")
        return False
    except Exception as e:
        print(f"General error for id_code {id_code} on column {col}: {str(e)}")
        log_message(f"Error for {id_code} on column {col} (General): {str(e)}")
        return False
    
# Function to process large datasets (more than 1 million rows)
def process_large_dataset(id_code: str, col: str) -> bool:
    """Process datasets with more than 1 million rows."""
    try:
        # Build query string dynamically based on col
        query = f"""
            SELECT 
                {col}, 
                count(*) AS count
            WHERE 
                LOWER({col}) LIKE '%flood%'
            GROUP BY 
                {col}
            ORDER BY 
                count DESC
        """

        # Fetch the query results from Socrata
        results = client.get(id_code, query=query)
        log_message(f"Processing {id_code}, column {col}")
        
        # Convert results to DataFrame
        df = pd.DataFrame(results)
        
        if df.empty:
            print(f"No relevant data in column {col} for {id_code}. Skipping.")
            log_message(f"No relevant data in column {col} for {id_code}. Skipping.")
            return False

        # Ensure the columns are named correctly
        df.columns = ['value', 'count']

        # Add timestamp, column name, and id_code to the DataFrame
        df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['column'] = col
        df['id'] = id_code

        # Append the results to the CSV file
        df.to_csv(output_csv, mode='a', header=False, index=False)
        print(f"Processed {id_code}, {col}")
        
        # Sleep for a brief moment to avoid overwhelming the API
        return True

    except requests.exceptions.RequestException as e:
        print(f"Request error for id_code {id_code} on column {col}: {str(e)}")
        log_message(f"Error for {id_code} on column {col} (RequestException): {str(e)}")
        return False
    except Exception as e:
        print(f"General error for id_code {id_code}: {str(e)}")
        log_message(f"Error for {id_code} (General): {str(e)}")
        return False

# Read the CSV with dataset definitions for both small and large datasets
dataset_ids_df = pd.read_csv("data/dataset-ids-columns.csv")  # For all datasets

# Open the output CSV for appending once before processing
if not os.path.exists(output_csv):
    pd.DataFrame(columns=['value', 'count', 'timestamp', 'column', 'id']).to_csv(output_csv, index=False)  # Create header if not exists

# Set to keep track of processed small datasets
processed_small_datasets = set()

# Process datasets
for id_code, column in zip(dataset_ids_df['id'], dataset_ids_df['columns_field_name']):
    # Skip large datasets that have already been processed as small datasets
    if id_code in processed_small_datasets:
        continue
    
    # First, count the number of rows in the dataset
    try:
        start_time = time.time()  # Track start time
        
        # Attempt to read the dataset size
        response = requests.get(f'https://data.cityofnewyork.us/resource/{id_code}.json?$select=count(*)', timeout=1200)
        response.raise_for_status()  # Ensure we catch HTTP errors
        
        count_df = pd.read_json(response.text)
        count = count_df.values[0][0]
        
        # Log and decide whether to process it as a small or large dataset
        log_message(f"Processing {id_code} - Row count: {count}")
        
        # If it took more than 20 minutes, skip this dataset
        elapsed_time = time.time() - start_time
        if elapsed_time > 1200:  # 20 minutes = 1200 seconds
            print(f"Row count query for {id_code} took too long ({elapsed_time/60:.2f} minutes). Skipping this dataset.")
            log_message(f"Row count query for {id_code} took too long. Skipping.")
            continue
        
        if count >= 1_000_000:
            process_large_dataset(id_code, column)
        else:
            process_small_dataset(id_code)
            # Add this small dataset ID to the set to avoid reprocessing
            processed_small_datasets.add(id_code)
        
        # Sleep for a brief moment to avoid overwhelming the API
        time.sleep(30)

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving row count for {id_code}: {str(e)}")
        log_message(f"Error for {id_code} (RequestException): {str(e)}")
        continue
    except Exception as e:
        print(f"Error processing {id_code}: {str(e)}")
        log_message(f"Error for {id_code} (General): {str(e)}")
        continue
