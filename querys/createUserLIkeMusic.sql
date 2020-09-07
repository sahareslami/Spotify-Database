create table userlikemusic(
username varchar(255),
musicId varchar(255),
primary key(username, musicId),
foreign key(username) references users(username)
on update cascade,
foreign key(musicId) references music(musicId)
on update cascade
)