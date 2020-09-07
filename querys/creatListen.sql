create table listen(
username varchar(255),
music varchar(255),
listenDate date,
primary key(music,userName),
foreign key(username) references users(username)
on update cascade,
foreign key(music) references music(musicId)
on update cascade
);