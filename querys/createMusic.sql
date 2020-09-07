create table music(
musicId varchar(255),
numberOfPlaying int default 0,
musicName varchar(255),
releasedDate date,
album varchar(255),
primary key(musicId),
foreign key (album) references album(albumName)
on delete set null
on update cascade
)
