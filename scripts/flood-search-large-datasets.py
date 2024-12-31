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

export_log = "logs/export-log-large-datasets.txt"
output_csv = "results/results-large-datasets.csv"

# Function to log dataset-column processing with a timestamp
def log_message(message: str) -> None:
    """Log messages with timestamp."""
    with open(export_log, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{message}\n")

# Function to process data and write to CSV
def process_and_write_to_csv(id_code: str, col: str) -> bool:
    """Process the query results and write to CSV."""
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
        
        # Convert results to DataFrame
        df = pd.DataFrame(results)
        
        if df.empty:
            print(f"No data available for {id_code} - {col}. Skipping.")
            log_message(f"Skipping {id_code} - {col} due to no data.")
            return False

        # Ensure the columns are named correctly
        df.columns = ['value', 'count']

        # Add timestamp, column name, and id_code to the DataFrame
        df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['column'] = col
        df['id'] = id_code

        # Append the results to the CSV file
        df.to_csv(output_csv, mode='a', header=False, index=False)
        print(f"Processed {id_code},{col}")

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
df = pd.read_csv("../data/dataset-ids-columns.csv")

# Open the output CSV for appending once before processing
if not os.path.exists(output_csv):
    pd.DataFrame(columns=['value', 'count', 'timestamp', 'column', 'id']).to_csv(output_csv, index=False)  # Create header if not exists

# Process each dataset ID
for id_code, column in zip(df['id'], df['columns_field_name']):
    # Log the dataset processing
    log_message(f"Processing {id_code} - {column}")
    
    # Process the data and write to CSV
    success = process_and_write_to_csv(id_code, column)
    
    if not success:
        print(f"Skipping {id_code} due to errors.")
    
    # Sleep for a brief moment to avoid overwhelming the API
    time.sleep(10)
