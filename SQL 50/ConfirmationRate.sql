WITH ConfirmationCounts AS (
  SELECT 
      user_id,
      COUNT(*) AS total_requests,
      SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_requests
  FROM 
      Confirmations
  GROUP BY 
      user_id
),
UserConfirmationRates AS (
  SELECT 
      s.user_id,
      COALESCE(confirmed_requests / total_requests, 0) AS confirmation_rate
  FROM 
      Signups s
  LEFT JOIN 
      ConfirmationCounts c ON s.user_id = c.user_id
)
SELECT 
  user_id,
  ROUND(confirmation_rate, 2) AS confirmation_rate
FROM 
  UserConfirmationRates
ORDER BY 
  user_id;