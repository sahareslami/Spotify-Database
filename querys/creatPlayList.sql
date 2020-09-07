create table playList(
playListId varchar(255) primary key,
creator varchar(255),
playListName varchar(255),
creationDate date,
foreign key(creator) references users(username)
on delete set null
on update cascade)