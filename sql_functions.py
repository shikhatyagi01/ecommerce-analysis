
import mysql.connector
from mysql import connector
from dotenv import load_dotenv
import pandas as pd


import os
load_dotenv()

user= os.getenv("USER")
password= os.getenv('PASSWORD')
host= os.getenv("HOST")

database="swiftmarket"

connection=connector.connect(
    user= user,
    password= password,
    host= host,
    database= database

)

cursor = connection.cursor()

def read_query(query):
    cursor.execute(query)
    rows=cursor.fetchall()
    return pd.DataFrame(data=rows,columns=cursor.column_names)


if __name__ =='__main__':
        
        query = "show tables;"
        print(query)
        df = read_query(query=query)
        print(df)


