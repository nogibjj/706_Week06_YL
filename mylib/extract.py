import requests
import pandas as pd

def extract(url1="https://raw.githubusercontent.com/fivethirtyeight/data/master/womens-world-cup-predictions/wwc-matches-20150602-093000.csv?raw=true",
            url2="https://raw.githubusercontent.com/fivethirtyeight/data/master/womens-world-cup-predictions/wwc-matches-20150705-205539.csv?raw=true",
            file_path1="data/wwc-matches-20150602-093000",
            file_path2="data/wwc-matches-20150705-205539"):
    with requests.get(url1) as r:
        with open(file_path1, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    
    df1 = pd.read_csv(file_path1).dropna().to_csv(file_path1, index=False)
    df2 = pd.read_csv(file_path2).dropna().to_csv(file_path2, index=False)

    return file_path1, file_path2