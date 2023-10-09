```sql
SELECT team AS Team, COUNT(*) AS MatchesPlayed 
FROM 
(SELECT team1 AS team FROM default.wwc0602
UNION ALL 
SELECT team2 AS team FROM default.wwc0602
UNION ALL
SELECT team1 AS team FROM default.wwc0705
UNION ALL
SELECT team2 AS team FROM default.wwc0705) AS TotalTeams
GROUP BY Team
ORDER BY MatchesPlayed DESC;
```