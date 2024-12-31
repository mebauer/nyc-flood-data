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

export_log = "logs/export-log.txt"
output_csv = "results/results.csv"

# Function to log dataset-column processing with a timestamp
def log_message(message: str) -> None:
    """Log messages with timestamp."""
    with open(export_log, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{message}\n")

# Function to process data and write to CSV
def process_and_write_to_csv(id_code: str, col:str) -> bool:
    """Process the query results and write to CSV."""
    try:
        # Attempt to read the dataset
        response = requests.get(f'https://data.cityofnewyork.us/resource/{id_code}.json?$select=count(*)')
        response.raise_for_status()  # Ensure we catch HTTP errors
        count_df = pd.read_json(response.text)
        count = count_df.values[0][0]
        
        if count >= 1_000_000:
            print(f"Skipping {id_code} due to too many rows.")
            log_message(f"Skipping {id_code} due to too many rows.")
            return False

        else:
            dataset_url = f"https://data.cityofnewyork.us/api/views/{id_code}/rows.csv?accessType=DOWNLOAD"
            results_df = pd.read_csv(dataset_url)

            if results_df.empty:
                print(f"No data available for {id_code}. Skipping.")
                log_message(f"Skipping {id_code} due to no data.")
                return False

            for col in results_df.columns:
                log_message(f"Processing {id_code},column {col}")

                # Ensure the column is of string type before applying str.contains
                if results_df[col].dtype != 'object':
                    results_df[col] = results_df[col].astype(str)

                # Identify rows where column contains 'flood' (case-insensitive)
                contains_flood_ser = (
                    results_df
                    .loc[results_df[col].str.contains('flood', case=False, na=False)][col]
                    .value_counts()
                )

                if contains_flood_ser.empty:
                    print(f"No relevant data in column {col} for {id_code}. Skipping.")
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
        print(f"General error for id_code {id_code}: {str(e)}")
        log_message(f"Error for {id_code} (General): {str(e)}")
        return False

# Read the CSV with column definitions
df = pd.read_csv("../data/dataset-ids.csv")

# Open the output CSV for appending once before processing
if not os.path.exists(output_csv):
    pd.DataFrame(columns=['value', 'count', 'timestamp', 'column', 'id']).to_csv(output_csv, index=False)  # Create header if not exists

# Process each dataset ID
for id_code in df['id'].to_list():
    # Log the dataset processing
    log_message(f"Processing {id_code}")
    
    # Process the data and write to CSV
    success = process_and_write_to_csv(id_code)
    
    if not success:
        print(f"Skipping {id_code} due to errors.")
    
    # Sleep for a brief moment to avoid overwhelming the API
    time.sleep(10)

