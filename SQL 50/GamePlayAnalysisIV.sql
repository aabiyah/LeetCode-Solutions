# Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

WITH FirstLogins AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),

ConsecutiveLogins AS (
    SELECT
        f.player_id
    FROM FirstLogins f
    JOIN Activity a
    ON f.player_id = a.player_id
    AND f.first_login_date = a.event_date

    JOIN Activity a_next
    ON f.player_id = a_next.player_id
    AND DATE_ADD(f.first_login_date, INTERVAL 1 DAY) = a_next.event_date
    GROUP BY f.player_id
),

TotalPlayers AS (
    SELECT COUNT(DISTINCT player_id) AS total_players
    FROM FirstLogins
),

PlayersWithConsecutiveLogins AS (
    SELECT COUNT(DISTINCT player_id) AS count_consecutive
    FROM ConsecutiveLogins
)

SELECT
    ROUND(
        (count_consecutive * 1.0 / total_players), 
        2
    ) AS fraction
FROM PlayersWithConsecutiveLogins, TotalPlayers;
