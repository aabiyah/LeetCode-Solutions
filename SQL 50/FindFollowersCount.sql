# Write a solution that will, for each user, return the number of followers. Return the result table ordered by user_id in ascending order.

SELECT 
    user_id,
    COUNT(follower_id) AS followers_count
FROM 
    Followers
GROUP BY 
    user_id
ORDER BY 
    user_id;