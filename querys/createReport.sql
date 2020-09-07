create table report(
username varchar(255),
musicId varchar(255),
primary Key (username, musicId),
foreign key (username) references users(username)
on update cascade,
foreign key (musicId) references music(musicId)
on update cascade
)