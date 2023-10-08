import os
import requests
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load(data1="data/wwc-matches-20150602-093000", 
         data2="data/wwc-matches-20150705-205539"):
    df1 = pd.read_csv(data1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(data2, delimiter=",", skiprows=1)

    load_dotenv()
    host = os.getenv("server_hostname")
    token = os.getenv("token")
    path = os.getenv("http_path")
    with sql.connect(server_hostname=host, access_token=token, http_path=path) as conn:
        c = conn.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'wwc0602'")
        result = c.fetchall()
        if not result:
            c.execute("""CREATE TABLE IF NOT EXISTS wwc0602(
                 id int,
                 date string,
                 group string,
                 team1 string,
                 team2 string,
                 team1_win real,
                 team2_win real,
                 tie real
            )""")
            for _, row in df1.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO wwc0602 VALUES{convert}")
            c.execute("SHOW TABLES FROM default LIKE 'wwc0602'")
            result = c.fetchall()
            
            if not result:
                c.execute("""CREATE TABLE IF NOT EXISTS wwc0705(
                 id int,
                 date string,
                 group string,
                 team1 string,
                 team2 string,
                 team1_win real,
                 team2_win real,
                 tie real
            )""")
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO wwc0705 VALUES{convert}")
            c.close()

    return "success"