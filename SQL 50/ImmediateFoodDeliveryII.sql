# If the customers preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled. The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order. Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

WITH FirstOrders AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),

ImmediateOrders AS (
    SELECT 
        d.customer_id,
        CASE
            WHEN d.order_date = d.customer_pref_delivery_date THEN 1
            ELSE 0
        END AS is_immediate
    FROM Delivery d
    JOIN FirstOrders fo
    ON d.customer_id = fo.customer_id
    AND d.order_date = fo.first_order_date
)

SELECT 
    ROUND(
        (SUM(is_immediate) * 100.0 / COUNT(*)), 
        2
    ) AS immediate_percentage
FROM ImmediateOrders;
