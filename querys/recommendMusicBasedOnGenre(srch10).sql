select musicName
from music as m, musicgenre as mg
where m.musicId = mg.musicId and mg.musicGenre = 'gheri' 
	and m.releasedDate < '2020-12-30' and m.releasedDate > '2020-12-23'