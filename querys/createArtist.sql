create table artist(
username varchar(255) primary key not null, 
artisticName varchar(255),
startDate date,
nationality varchar(255),
isConfirmed boolean default null,
adminConfirmed varchar(255),
FOREIGN KEY (adminConfirmed) REFERENCES admin(username)
on delete set NUll
on update cascade
)