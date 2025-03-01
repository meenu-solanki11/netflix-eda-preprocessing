import psycopg2
import pandas as pd
from datetime import datetime

# PostgreSQL connection details
db_params = {
    "dbname": "netflix_pre_processing",
    "user": "postgres",
    "password": "password123",
    "host": "localhost",
    "port": "5432"
}

# Load CSV file
file_path = r"C:\Users\AIR FORCE COMPUTER\Desktop\Projects\SQL Project(With Tableau)\Netflix Dataset\Netflix Dataset (Raw).csv"
df = pd.read_csv(file_path)

# Replace 'NaN' with None for proper NULL handling in PostgreSQL
df = df.where(pd.notna(df), None)

# Convert `release_date` column to proper DATE format
def parse_date(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, "%B %d, %Y").date()
        except ValueError:
            return None  # Return None if conversion fails
    return None

df["Release_Date"] = df["Release_Date"].apply(parse_date)

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Insert data using batch execution for better performance
insert_query = """
    INSERT INTO netflix2021 (show_id, category, title, director, cast_members, country, release_date, rating, duration, type, description) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (show_id) DO NOTHING;
"""

data_tuples = [(
    row["Show_Id"], row["Category"], row["Title"], row["Director"], row["Cast_members"], 
    row["Country"], row["Release_Date"], row["Rating"], row["Duration"], row["Type"], row["Description"]
) for _, row in df.iterrows()]

cur.executemany(insert_query, data_tuples)

# Commit and close
conn.commit()
cur.close()
conn.close()

print("CSV data inserted successfully!")
