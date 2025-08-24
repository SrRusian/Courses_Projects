SELECT artist, avg(plays)
FROM playlist
GROUP BY artist;