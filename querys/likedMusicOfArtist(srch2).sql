select m.musicName, count(ulm.musicId)
from music as m, userlikemusic as ulm
where m.musicId = ulm.musicId and m.artist = 'sahar'
group by(ulm.musicId)
