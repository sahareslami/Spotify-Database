select m.musicName, phm.addedDate, m.duration
from palylisthavemusic as phm, music as m
where phm.playListId = 'shivaPlaylist' and phm.musicId = m.musicId