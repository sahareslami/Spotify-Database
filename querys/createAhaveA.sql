create table artistHaveAlbum(
artistName varchar(255),
albumName varchar(255),
primary key(artistName, albumNAme),
foreign key(artistName) references artist(userName)
on update cascade,
foreign key(albumName) references album(albumName)
on update cascade)