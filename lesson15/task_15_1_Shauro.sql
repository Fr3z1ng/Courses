SELECT sum(Bytes) FROM tracks
#############################
SELECT SUM (sum_count) FROM (SELECT count(*) as sum_count from employees UNION SELECT count(*) as sum_count from customers)
#############################
SELECT Name FROM tracks where AlbumId = (SELECT AlbumId FROM albums where Title = 'A-Sides')
#############################
SELECT Title as Name, AlbumPrice as Price
from albums
INNER JOIN ( 
SELECT SUM(UnitPrice) as AlbumPrice,AlbumId
from tracks
GROUP BY(AlbumId)
)
USING(AlbumId)