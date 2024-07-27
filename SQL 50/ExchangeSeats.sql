# Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped. Return the result table ordered by id in ascending order.

WITH SwappedSeats AS (
    SELECT 
        CASE 
            WHEN MOD(id, 2) = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
            WHEN MOD(id, 2) = 0 THEN id - 1
            ELSE id
        END AS new_id,
        student
    FROM Seat
)
SELECT 
    new_id AS id,
    student
FROM 
    SwappedSeats
ORDER BY 
    id;
