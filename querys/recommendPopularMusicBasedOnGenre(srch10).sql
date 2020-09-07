select musicName, count(l.music)
from listen as l, music as m, musicgenre as mg
where l.music = m.musicId and m.musicId = mg.musicId and mg.musicGenre = 'classic'
group by(l.music)
