# Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount. Return the result table in any order. 

SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    Products p
JOIN
    Orders o
ON
    p.product_id = o.product_id
WHERE
    o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY
    p.product_name
HAVING
    SUM(o.unit) >= 100;
