create table Users(
username varchar(255) primary key not null, 
email varchar(255) unique not null,
listeningTime int default 0,
pass varchar(255) not null,
question enum('q1', 'q2', 'q3', 'q4'),
answer varchar(255),
userType enum('listener', 'artist', 'admin')
)