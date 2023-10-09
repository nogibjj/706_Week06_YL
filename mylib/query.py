import os
from databricks import sql
from dotenv import load_dotenv

log_file = "query.md"

def log_query(query, result="none"):
    with open(log_file, "a") as f:
        f.write(f"```sql\n{query}\n```\n\n")
        f.write(f"```response from databricks \n{result}\n```\n\n")

def Query(query):
    load_dotenv()
    server = os.getenv("server_hostname")
    access_token = os.getenv("access_token")
    http_path = os.getenv("http_path")
    with sql.connect(
        server_hostname=server,
        http_path=http_path,
        access_token=access_token
    ) as conn:
        c= conn.cursor()
        c.execute(query)
        result = c.fetchall()
        c.close()
    
    log_query(f"{query}", result)