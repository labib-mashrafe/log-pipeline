SELECT ip, COUNT(DISTINCT user) AS users, COUNT(*) AS failures
FROM events
WHERE event = 'failed_password'
GROUP BY ip
ORDER BY users DESC;