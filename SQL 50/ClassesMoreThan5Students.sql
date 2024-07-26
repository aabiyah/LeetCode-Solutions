# Write a solution to find all the classes that have at least five students. Return the result table in any order.

SELECT 
    class
FROM 
    Courses
GROUP BY 
    class
HAVING 
    COUNT(student) >= 5;