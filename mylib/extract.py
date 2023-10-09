import requests

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

    return file_path1, file_path2