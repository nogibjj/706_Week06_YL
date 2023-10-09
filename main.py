import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import Query

def add_action(args):
    parser = argparse.ArgumentParser(description="Complex SQL query")
    parser.add_argument("action", choices=["extract", "transform_load", "general_query"])
    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "general_query":
        parser.add_argument("query")

    return parser.parse_args(sys.argv[:1])

def main():
    args = add_action(sys.argv[:1])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "general_query":
        print("Executing the query...")
        Query(args.query)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()