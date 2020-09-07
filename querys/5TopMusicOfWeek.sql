select music, count(music)
from listen
where listenDate > '2020-12-10' and listenDate < '2020-12-30'
group by(music)
