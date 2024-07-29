# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

SELECT
    MAX(salary) AS SecondHighestSalary
FROM
    Employee
WHERE
    salary < (SELECT MAX(salary) FROM Employee);