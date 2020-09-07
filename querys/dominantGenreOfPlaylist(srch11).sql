select mg.musicGenre, count(phm.musicId)
from playlist as p, palylisthavemusic as phm, musicgenre as mg
where p.playListId = phm.playListId and mg.musicId = phm.musicId and p.playListId = 'shivaPlayLIst'
group by(musicGenre)