select mg.musicGenre, count(l.music)
from listen as l, music as m, musicgenre as mg
where l.music = m.musicId and mg.musicId = m.musicId
	and l.username = 'shiva'
group by(mg.musicGenre)