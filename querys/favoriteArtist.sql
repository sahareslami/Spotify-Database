select m.artist, count(musicId)
from listen as l, music as m
where l.username = 'shiva'
group by(m.artist)