# Write a solution to: Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name. Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name. The result format is in the following example.

WITH UserRatings AS (
    SELECT 
        u.name, 
        COUNT(mr.movie_id) AS rating_count
    FROM 
        Users u
    JOIN 
        MovieRating mr ON u.user_id = mr.user_id
    GROUP BY 
        u.name
),
TopUser AS (
    SELECT 
        name
    FROM 
    UserRatings
    ORDER BY 
        rating_count DESC, 
        name ASC
    LIMIT 1
),
FebruaryRatings AS (
    SELECT 
        mr.movie_id, 
        AVG(mr.rating) AS avg_rating
    FROM 
        MovieRating mr
    WHERE 
        mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY 
        mr.movie_id
),
TopMovie AS (
    SELECT 
        m.title
    FROM 
        FebruaryRatings fr
    JOIN 
        Movies m ON fr.movie_id = m.movie_id
    ORDER BY 
        fr.avg_rating DESC, 
        m.title ASC
    LIMIT 1
)
SELECT 
    t.name AS results
FROM 
    TopUser t
UNION ALL
SELECT 
    t.title AS results
FROM 
    TopMovie t;

