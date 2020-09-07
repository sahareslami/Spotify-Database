select aha.artistName, ag.albumGenre
from albumgenre as ag, artisthavealbum as aha
where ag.albumName = aha.albumName
group by (artistName)