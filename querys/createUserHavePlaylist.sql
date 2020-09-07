create table userhaveplaylist(
playLIstId varchar(255),
username varchar(255),
primary key(playListId, username),
foreign key(playListId) references playList(playLIstId)
on update cascade,
foreign key(username) references users(username)
on update cascade
)