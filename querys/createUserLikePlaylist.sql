create table userLikePlayList(
playlistId varchar(255),
username varchar(255),
primary key(playlistId, username),
foreign key(playlistId) references playlist(playListId)
on update cascade,
foreign key(username) references users(username)
on update cascade
)