create table Listener(
username varchar(255) primary key not null, 
yearOfBearth int,
firstName varchar(255),
lastName varchar(255),
nationality varchar(255),
listenerType enum('free', 'premium') default 'free'
)