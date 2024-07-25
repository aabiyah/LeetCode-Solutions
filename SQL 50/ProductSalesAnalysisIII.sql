#Write a solution to select the product id, year, quantity, and price for the first year of every product sold. Return the resulting table in any order.

WITH FirstSale AS (
    SELECT 
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT 
    s.product_id,
    f.first_year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN FirstSale f 
    ON s.product_id = f.product_id AND s.year = f.first_year;
