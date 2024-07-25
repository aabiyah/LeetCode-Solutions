# Write a solution to find the percentage of the users registered in each contest rounded to two decimals. Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

WITH TotalUsers AS (
    SELECT COUNT(*) AS total_users
    FROM Users
),
ContestRegistrations AS (
    SELECT
        contest_id,
        COUNT(*) AS registered_users
    FROM Register
    GROUP BY contest_id
)
SELECT
    cr.contest_id,
    ROUND((cr.registered_users * 100.0 / tu.total_users), 2) AS percentage
FROM
    ContestRegistrations cr,
    TotalUsers tu
ORDER BY
    percentage DESC,
    contest_id ASC;
