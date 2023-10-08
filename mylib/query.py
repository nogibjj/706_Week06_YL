import os
from databricks import sql
from dotenv import load_dotenv

log_file = "query.md"

def log_query(query, result="none"):
    with open(log_file, "a") as f:
        f.write(f"```sql\n{query}\n```\n\n")
        f.write(f"```response from databricks \n{result}\n```\n\n")