SELECT ip, substr(ts, 12, 2) AS hour, COUNT(*) AS failures
FROM events
WHERE event = 'failed_password'
GROUP BY ip, hour
ORDER BY failures DESC;