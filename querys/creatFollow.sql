create table follow(
follower varchar(255),
followed varchar(255),
primary key(follower, followed),
foreign key (follower) references users(username)
on update cascade,
foreign key (followed) references users(username)
on update cascade
);