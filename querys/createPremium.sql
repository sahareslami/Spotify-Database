create table premium(
username varchar(255) primary key not null, 
subscriptionType enum('3 Monnth', '6 Month', '1 Year'),
subscreationDate date,
cardNumber int not null,
cardExpirationDate date not null
)