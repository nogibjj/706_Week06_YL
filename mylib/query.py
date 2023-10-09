import os
from databricks import sql
from dotenv import load_dotenv

log_file = "query.md"

def log_query(query, result="none"):
    with open(log_file, "a") as f:
        f.write(f"```sql\n{query}\n```\n\n")
        f.write(f"```response from databricks \n{result}\n```\n\n")

def Query():
    load_dotenv()
    server = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server,
        http_path=http_path,
        access_token=access_token
    ) as conn:
        c= conn.cursor()
        query = """SELECT team AS Team, COUNT(*) AS MatchesPlayed 
        FROM 
        (SELECT team1 AS team FROM default.wwc0602
        UNION ALL 
        SELECT team2 AS team FROM default.wwc0602
        UNION ALL
        SELECT team1 AS team FROM default.wwc0705
        UNION ALL
        SELECT team2 AS team FROM default.wwc0705) AS TotalTeams
        GROUP BY Team
        ORDER BY MatchesPlayed DESC;"""
        c.execute(query)
        result = c.fetchall()
        c.close()
    
    log_query(f"{query}", result)