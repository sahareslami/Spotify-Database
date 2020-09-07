select aha.albumName , a.releasedDate
from artisthavealbum as aha, album as a
where  aha.artistName = 'sahar' and aha.albumName = a.albumName