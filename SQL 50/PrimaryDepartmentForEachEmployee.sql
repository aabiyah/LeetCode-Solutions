# Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'. Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department. Return the result table in any order.

SELECT 
    employee_id,
    department_id
FROM 
    Employee
WHERE 
    primary_flag = 'Y'
UNION
SELECT 
    employee_id,
    department_id
FROM 
    Employee
WHERE 
    employee_id NOT IN (SELECT employee_id FROM Employee WHERE primary_flag = 'Y')
ORDER BY 
    employee_id;
