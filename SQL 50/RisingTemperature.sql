SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE 
    w1.temperature > w2.temperature;

# The query joins the Weather table (w1) with itself (w2) where the recordDate of w1 is one day after the recordDate of w2 (w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)).