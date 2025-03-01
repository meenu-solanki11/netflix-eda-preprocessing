# Netflix Data Analysis using MySQL and Python

## Project Overview
This project focuses on processing and analyzing Netflix data using MySQL and Python (Pandas, SQLAlchemy). The dataset is stored in a MySQL database and loaded from a CSV file for further analysis. 

## Technologies Used
- **Python** (pandas, SQLAlchemy, pymysql)
- **MySQL** (Database for storing Netflix data)
- **Power BI/Tableau** (For visualization, if applicable)

## Project Structure
```
📂 SQL Project (With Tableau)/
│-- 📂 Netflix Dataset/
│   │-- Netflix.csv
│-- 📜 MySQL.sql (Database schema and queries)
│-- 📜 data_loader.py (Python script to load CSV into MySQL)
│-- 📜 README.md (This file)
```

## Setup Instructions
### 1. Install Dependencies
Ensure you have Python installed along with the required libraries:
```sh
pip install pandas sqlalchemy pymysql
```

### 2. Setup MySQL Database
1. Start MySQL Server.
2. Create the database manually using MySQL Workbench or command line:
   ```sql
   CREATE DATABASE Netflix_pre_processing;
   ```
3. Use the provided `MySQL.sql` file to set up tables and insert data.
   ```sh
   mysql -u root -p Netflix_pre_processing < MySQL.sql
   ```

### 3. Load Data into MySQL
Run the `MySQL_Connection.py` script to insert the Netflix dataset into MySQL:
```sh
python MySQL_Connection.py
```

## Python Script Explanation (`MySQL_Connection.py`)
This script reads the `Netflix.csv` file and inserts the data into MySQL.
```python
import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
conn_string = 'mysql+pymysql://root:password123@127.0.0.1/Netflix_pre_processing'
db = create_engine(conn_string)
conn = db.connect()

# Load CSV into MySQL
file_path = "C:/Users/AIR FORCE COMPUTER/Desktop/Projects/SQL Project(With Tableau)/Netflix Dataset/Netflix.csv"
df = pd.read_csv(file_path, encoding="utf-8")
df.to_sql("Netflix", con=conn, if_exists='replace', index=False)
conn.close()
```

## Future Improvements
- Add data cleaning and preprocessing steps.
- Create advanced SQL queries for analysis.
- Integrate with Power BI/Tableau for visualization.

## Author
Your Name - [GitHub Profile](https://github.com/yourgithub)


