create table musicGenre(
musicId varchar(255),
musicGenre varchar(255),
primary key(musicId , musicGenre),
foreign key(musicId) references music(musicId)
on update cascade
)