select sum(m.duration)
from listen as l, music as m
where l.music = m.musicId and l.listenDate = '2020-12-12'
group by(l.username)