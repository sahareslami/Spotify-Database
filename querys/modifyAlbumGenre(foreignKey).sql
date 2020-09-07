ALTER TABLE albumgenre
ADD foreign  KEY (albumName) references album(albumName)
on update cascade