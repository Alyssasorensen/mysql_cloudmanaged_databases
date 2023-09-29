import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect


"""

It also uses python-dotenv for bringing in secrets from your .env file 

The default port is set to 3306 for MySQL, but you can override it by 
modifying the DB_PORT in your .env file.

The connection string is MySQL-specific, incorporating the specified port and charset.

"""

#import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("alyssacloud504hw:us-central1:alyssa-hwtest")
DB_DATABASE = os.getenv("gcp hw instance")
DB_USERNAME = os.getenv("Alyssa.sorensen@stonybrook.edu")
DB_PASSWORD = os.getenv("***")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = f"mysql+pymysql://{Alyssa.sorensen@stonybrook.edu}:{***}@{alyssacloud504hw:us-central1:alyssa-hwtest}:{3306}/{gcp hw instance}?charset={utf8mb4}"

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

# Define a function to insert dummy data into a table
def insert_dummy_data(engine, table_name):
    data = [
        {"column1": "value1", "column2": 123},
        {"column1": "value2", "column2": 456},
        # Add more dummy data as needed
    ]
    df = pd.DataFrame(data)
    df.to_sql(table_name, engine, if_exists="replace", index=False)

# Define a function to retrieve data from a table and store it in a DataFrame
def retrieve_data(engine, table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    # Modify this to specify the table you want to work with
    table_name = "data_table"
    
    # Insert dummy data into the table
    insert_dummy_data(db_engine, table_name)
    
    # Retrieve data from the table and store it in a DataFrame
    data_df = retrieve_data(db_engine, table_name)
    
    # Print the retrieved data
    print(data_df)
