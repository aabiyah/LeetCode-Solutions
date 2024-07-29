-- A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

-- Write a solution to find the employees who are high earners in each of the departments.

-- Return the result table in any order.

WITH TopSalaries AS (
    SELECT departmentId, salary
    FROM (
        SELECT departmentId, salary,
               DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
        FROM Employee
    ) ranked_salaries
    WHERE rnk <= 3
)
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, salary
    FROM TopSalaries
)
ORDER BY Department, Salary DESC, Employee;
