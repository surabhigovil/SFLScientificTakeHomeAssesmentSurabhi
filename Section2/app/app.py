import time
import random

from sqlalchemy import create_engine

import pandas as pd

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'
db_table = 'users'
# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

file_path = "/home/surabhi/assessment/SFLScientificTakeHomeAssesmentSurabhi/Section2/data/DATA.csv"

def extract_from_csv(file_to_process):
  dataframe = pd.read_csv(file_to_process)
  return dataframe

def extract():
  extracted_data = pd.DataFrame(columns = ["id", "first_name", "last_name", "email", "gender", "ip_address"])
  
  extracted_data = extracted_data.append(extract_from_csv(file_path), ignore_index=True)
 
  return extracted_data
 

def add_new_row(df):

    """
    Loads a pandas DataFrame to a bit.io database.
    Parameters
    ----------
    df : pandas.DataFrame
    destination : str
        Fully qualified bit.io PostgreSQL table name.
    pg_conn_string : str
        A bit.io PostgreSQL connection string including credentials.
    """

    with db.connect() as conn:
        conn.execute("SET statement_timeout = 600000;")
        df.to_sql(
            db_table,db)

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT * " + \
            "FROM users " +\
            "LIMIT 1"

    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

if __name__ == '__main__':
    print('Application started')
    
    while True:
        time.sleep(5)
        data = extract()
        add_new_row(data)
        print('The last value insterted is: {}'.format(get_last_row()))