# Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer. Return the result table ordered by employee_id.

SELECT 
    e1.employee_id,
    e1.name,
    COUNT(e2.employee_id) AS reports_count,
    ROUND(AVG(e2.age)) AS average_age
FROM 
    Employees e1
LEFT JOIN 
    Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY 
    e1.employee_id, e1.name
HAVING 
    COUNT(e2.employee_id) > 0
ORDER BY 
    e1.employee_id;
