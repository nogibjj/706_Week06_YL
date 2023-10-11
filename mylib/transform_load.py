import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load(data1="data/wwc-matches-20150602-093000", 
         data2="data/wwc-matches-20150705-205539"):
    df1 = pd.read_csv(data1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(data2, delimiter=",", skiprows=1)

    load_dotenv()
    host = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(server_hostname=host, access_token=token, http_path=path) as conn:
        c = conn.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'wwc_0602'")
        result = c.fetchall()
        if not result:
            c.execute("""CREATE TABLE IF NOT EXISTS wwc_0602(
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
                c.execute(f"INSERT INTO wwc_0602 VALUES{convert}")
            c.execute("SHOW TABLES FROM default LIKE 'wwc_0602'")
            result = c.fetchall()
            
            if not result:
                c.execute("""CREATE TABLE IF NOT EXISTS wwc_0705(
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
                c.execute(f"INSERT INTO wwc_0705 VALUES{convert}")
            c.close()

    return "success"