import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Obtaining credentials and connection details from environment variables
db_url = os.getenv('DATABASE_URL')

# Connect to PostgreSQL
engine = create_engine(db_url)

# Get CSV path from environment variables
csv_path = os.getenv('CSV_PATH')

# Read CSV file
df = pd.read_csv(csv_path)

# Clean null or invalid data and conversion in the 'date' column
df.dropna(inplace=True) 
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Create the table automatically and import the data
df.to_sql('sales', engine, index=False, if_exists='replace')

print("Table created and data imported successfully.")
