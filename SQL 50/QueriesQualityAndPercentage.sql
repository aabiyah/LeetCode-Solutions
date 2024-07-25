# Write a solution to find each query_name, the quality and poor_query_percentage. Both quality and poor_query_percentage should be rounded to 2 decimal places. Return the result table in any order.

WITH QueryStats AS (
    SELECT
        query_name,
        AVG(rating * 1.0 / position) AS quality,
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS poor_query_percentage
    FROM Queries
    GROUP BY query_name
)

SELECT
    query_name,
    ROUND(quality, 2) AS quality,
    ROUND(poor_query_percentage, 2) AS poor_query_percentage
FROM QueryStats
WHERE query_name IS NOT NULL;
