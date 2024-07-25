#Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. Return the result table in any order.

WITH TotalSales AS (
    SELECT
        us.product_id,
        SUM(us.units * p.price) AS total_revenue,
        SUM(us.units) AS total_units
    FROM
        UnitsSold us
    JOIN
        Prices p
    ON
        us.product_id = p.product_id
        AND us.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY
        us.product_id
),
AllProducts AS (
    SELECT product_id FROM Prices
    UNION
    SELECT product_id FROM UnitsSold
)

SELECT
    ap.product_id,
    ROUND(COALESCE(ts.total_revenue, 0) / COALESCE(NULLIF(ts.total_units, 0), 1), 2) AS average_price
FROM
    AllProducts ap
LEFT JOIN
    TotalSales ts
ON
    ap.product_id = ts.product_id
ORDER BY
    ap.product_id;
