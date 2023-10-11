from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import Query

print("Extracting data...")
extract()

print("Transforming data...")
load()

if __name__ == "__main__":
    Query()
