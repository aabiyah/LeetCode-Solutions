# Write a solution to find the people who have the most friends and the most friends number. The test cases are generated so that only one person has the most friends.

WITH AllFriends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
FriendCounts AS (
    SELECT 
        id,
        COUNT(*) AS num
    FROM AllFriends
    GROUP BY id
)
SELECT 
    id, 
    num
FROM FriendCounts
ORDER BY num DESC
LIMIT 1;
