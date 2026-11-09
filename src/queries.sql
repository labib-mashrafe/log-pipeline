SELECT substr(ts, 12, 2) AS hour, COUNT(*) AS failures
FROM events
WHERE event = 'failed_password'
GROUP BY hour
ORDER BY hour;