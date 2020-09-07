select a.username, count(musicId)
from artist as a, music as m
where a.username = m.artist
group by(a.username)