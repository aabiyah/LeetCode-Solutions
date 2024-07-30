# Find all numbers that appear at least three times consecutively. Return the result table in any order.

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.num = l2.num AND l1.id = l2.id - 1
JOIN Logs l3 ON l1.num = l3.num AND l2.id = l3.id - 1;