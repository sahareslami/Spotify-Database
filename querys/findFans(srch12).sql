select l.username, count(musicId)
from listen as l, music as m
where l.music = m.musicId and artist = 'kasra'
group by(l.username)