import subprocess

def test_extract():
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True
    )
    assert "Extracting data..." in result.stdout

def test_transform_load():
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True
    )
    assert "Transforming data..." in result.stdout

def test_Query():
    result = subprocess.run(
        ["python", "main.py", "general_query",
         """SELECT team AS Team, COUNT(*) AS MatchesPlayed 
         FROM 
         (SELECT team1 AS team FROM default.wwc0602
         UNION ALL 
         SELECT team2 AS team FROM default.wwc0602
         UNION ALL
         SELECT team1 AS team FROM default.wwc0705
         UNION ALL
         SELECT team2 AS team FROM default.wwc0705) AS TotalTeams
         GROUP BY Team
         ORDER BY MatchesPlayed DESC;"""],
         capture_output=True,
         text=True,
         check=True
    )
    assert "Executing the query..." in result.stdout