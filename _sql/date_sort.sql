WITH RECURSIVE dates(date) AS (
  SELECT DATE('2023-06-01') AS date
  UNION ALL
  SELECT DATE(date, '+1 day')
  FROM dates
  WHERE date < DATE('2023-07-03')
)
SELECT dates.date, prices.flat_id, flats.url, prices.price
FROM dates
LEFT JOIN prices ON dates.date = prices.date
LEFT JOIN flats ON flats.id = prices.flat_id
ORDER BY dates.date, prices.flat_id;