```sql
SELECT team AS Team, COUNT(*) AS MatchesPlayed 
        FROM 
        (SELECT team1 AS team FROM default.wwc_0602
        UNION ALL 
        SELECT team2 AS team FROM default.wwc_0602
        UNION ALL
        SELECT team1 AS team FROM default.wwc_0705
        UNION ALL
        SELECT team2 AS team FROM default.wwc_0705) AS TotalTeams
        GROUP BY Team
        ORDER BY MatchesPlayed DESC;
```

```response from databricks 
[Row(Team='USA', MatchesPlayed=10), Row(Team='England', MatchesPlayed=10), Row(Team='Japan', MatchesPlayed=10), Row(Team='Germany', MatchesPlayed=10), Row(Team='Australia', MatchesPlayed=8), Row(Team='China', MatchesPlayed=8), Row(Team='Canada', MatchesPlayed=8), Row(Team='France', MatchesPlayed=8), Row(Team='Cameroon', MatchesPlayed=7), Row(Team='South Korea', MatchesPlayed=7), Row(Team='Switzerland', MatchesPlayed=7), Row(Team='Netherlands', MatchesPlayed=7), Row(Team='Colombia', MatchesPlayed=7), Row(Team='Norway', MatchesPlayed=7), Row(Team='Brazil', MatchesPlayed=7), Row(Team='Sweden', MatchesPlayed=7), Row(Team='Ivory Coast', MatchesPlayed=6), Row(Team='Nigeria', MatchesPlayed=6), Row(Team='Thailand', MatchesPlayed=6), Row(Team='Spain', MatchesPlayed=6), Row(Team='Costa Rica', MatchesPlayed=6), Row(Team='Ecuador', MatchesPlayed=6), Row(Team='New Zealand', MatchesPlayed=6), Row(Team='Mexico', MatchesPlayed=6)]
```

```sql
SELECT team AS Team, COUNT(*) AS MatchesPlayed 
        FROM 
        (SELECT team1 AS team FROM default.wwc_0602
        UNION ALL 
        SELECT team2 AS team FROM default.wwc_0602
        UNION ALL
        SELECT team1 AS team FROM default.wwc_0705
        UNION ALL
        SELECT team2 AS team FROM default.wwc_0705) AS TotalTeams
        GROUP BY Team
        ORDER BY MatchesPlayed DESC;
```

```response from databricks 
[Row(Team='USA', MatchesPlayed=10), Row(Team='England', MatchesPlayed=10), Row(Team='Japan', MatchesPlayed=10), Row(Team='Germany', MatchesPlayed=10), Row(Team='Australia', MatchesPlayed=8), Row(Team='China', MatchesPlayed=8), Row(Team='Canada', MatchesPlayed=8), Row(Team='France', MatchesPlayed=8), Row(Team='Cameroon', MatchesPlayed=7), Row(Team='South Korea', MatchesPlayed=7), Row(Team='Switzerland', MatchesPlayed=7), Row(Team='Netherlands', MatchesPlayed=7), Row(Team='Colombia', MatchesPlayed=7), Row(Team='Norway', MatchesPlayed=7), Row(Team='Brazil', MatchesPlayed=7), Row(Team='Sweden', MatchesPlayed=7), Row(Team='Ivory Coast', MatchesPlayed=6), Row(Team='Nigeria', MatchesPlayed=6), Row(Team='Thailand', MatchesPlayed=6), Row(Team='Spain', MatchesPlayed=6), Row(Team='Costa Rica', MatchesPlayed=6), Row(Team='Ecuador', MatchesPlayed=6), Row(Team='New Zealand', MatchesPlayed=6), Row(Team='Mexico', MatchesPlayed=6)]
```

```sql
SELECT team AS Team, COUNT(*) AS MatchesPlayed 
        FROM 
        (SELECT team1 AS team FROM default.wwc_0602
        UNION ALL 
        SELECT team2 AS team FROM default.wwc_0602
        UNION ALL
        SELECT team1 AS team FROM default.wwc_0705
        UNION ALL
        SELECT team2 AS team FROM default.wwc_0705) AS TotalTeams
        GROUP BY Team
        ORDER BY MatchesPlayed DESC;
```

```response from databricks 
[Row(Team='USA', MatchesPlayed=10), Row(Team='England', MatchesPlayed=10), Row(Team='Japan', MatchesPlayed=10), Row(Team='Germany', MatchesPlayed=10), Row(Team='Australia', MatchesPlayed=8), Row(Team='China', MatchesPlayed=8), Row(Team='Canada', MatchesPlayed=8), Row(Team='France', MatchesPlayed=8), Row(Team='Cameroon', MatchesPlayed=7), Row(Team='South Korea', MatchesPlayed=7), Row(Team='Switzerland', MatchesPlayed=7), Row(Team='Netherlands', MatchesPlayed=7), Row(Team='Colombia', MatchesPlayed=7), Row(Team='Norway', MatchesPlayed=7), Row(Team='Brazil', MatchesPlayed=7), Row(Team='Sweden', MatchesPlayed=7), Row(Team='Ivory Coast', MatchesPlayed=6), Row(Team='Nigeria', MatchesPlayed=6), Row(Team='Thailand', MatchesPlayed=6), Row(Team='Spain', MatchesPlayed=6), Row(Team='Costa Rica', MatchesPlayed=6), Row(Team='Ecuador', MatchesPlayed=6), Row(Team='New Zealand', MatchesPlayed=6), Row(Team='Mexico', MatchesPlayed=6)]
```

```sql
SELECT team AS Team, COUNT(*) AS MatchesPlayed 
        FROM 
        (SELECT team1 AS team FROM default.wwc_0602
        UNION ALL 
        SELECT team2 AS team FROM default.wwc_0602
        UNION ALL
        SELECT team1 AS team FROM default.wwc_0705
        UNION ALL
        SELECT team2 AS team FROM default.wwc_0705) AS TotalTeams
        GROUP BY Team
        ORDER BY MatchesPlayed DESC;
```

```response from databricks 
[Row(Team='USA', MatchesPlayed=10), Row(Team='England', MatchesPlayed=10), Row(Team='Japan', MatchesPlayed=10), Row(Team='Germany', MatchesPlayed=10), Row(Team='Australia', MatchesPlayed=8), Row(Team='China', MatchesPlayed=8), Row(Team='Canada', MatchesPlayed=8), Row(Team='France', MatchesPlayed=8), Row(Team='Cameroon', MatchesPlayed=7), Row(Team='South Korea', MatchesPlayed=7), Row(Team='Switzerland', MatchesPlayed=7), Row(Team='Netherlands', MatchesPlayed=7), Row(Team='Colombia', MatchesPlayed=7), Row(Team='Norway', MatchesPlayed=7), Row(Team='Brazil', MatchesPlayed=7), Row(Team='Sweden', MatchesPlayed=7), Row(Team='Ivory Coast', MatchesPlayed=6), Row(Team='Nigeria', MatchesPlayed=6), Row(Team='Thailand', MatchesPlayed=6), Row(Team='Spain', MatchesPlayed=6), Row(Team='Costa Rica', MatchesPlayed=6), Row(Team='Ecuador', MatchesPlayed=6), Row(Team='New Zealand', MatchesPlayed=6), Row(Team='Mexico', MatchesPlayed=6)]
```

