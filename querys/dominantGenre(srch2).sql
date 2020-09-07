
select albumGenre as genre , count(ag.albumGenre) as count
from artisthavealbum as aHaveA, albumgenre as ag
where aHaveA.albumName = ag.albumName and aHaveA.artistName = 'sahar'
group by(ag.albumGenre) 

					  