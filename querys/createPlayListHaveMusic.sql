create table palylistHaveMusic(
playListId varchar(255),
musicId varchar(255),
addedDate date,
primary key(playListId, musicId),
foreign key(playLIstId) references playList(playListId)
on update cascade,
foreign key(musicId) references music(musicId)
on update cascade
)