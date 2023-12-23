/*creating database*/
create database social_media;
use social_media;

/*creating table for users*/
create table users(
user_id int primary key auto_increment,
username varchar(30) not null,
password varchar(30) not null,
first_name varchar(30) not null,
last_name varchar(30) not null,
email varchar(50),
birthdate date,
gender varchar(6),
nbr_of_friends int default 0,
nbr_of_posts int default 0,
phonenumber varchar(12),
unique(username),
unique(email)
);
alter table users
auto_increment = 1;
/*creating table for posts*/
create table posts(
post_id int primary key auto_increment,
content text,
nbr_of_likes int default 0,
nbr_of_shares int default 0,
nbr_of_comments int default 0,
nbr_of_views int default 0,
user_id int,
timestamp timestamp default current_timestamp,
foreign key(user_id) references users(user_id)
);
alter table posts
auto_increment=1;

/*creating messages table*/
create table messages(
message_id int primary key auto_increment,
m_content text,
m_timestamp timestamp,
receiver_id int NOT NULL,
sender_id int NOT NULL,
foreign key(receiver_id) references users(user_id),
foreign key(sender_id) references users(user_id) );

alter table messages
auto_increment=1;

/*creating reactios table*/
create table reactions(
post_id int ,
user_id int ,
type char(20) NOT NULL,
r_timestamp timestamp,
foreign key(user_id) references users(user_id),
foreign key(post_id) references posts(post_id));

/*creating comments table*/
create table comments(
post_id int,
user_id int,
content char(200) NOT NULL,
c_timestamp timestamp,
foreign key(user_id) references users(user_id),
foreign key(post_id) references posts(post_id));

ALTER TABLE comments
MODIFY c_timestamp timestamp DEFAULT current_timestamp;

select* from comments;
INSERT INTO users (first_name,last_name,email,phonenumber,birthdate,gender,username, password) values ('nour','adel','nouradel@gmail.com','01568291','2004/02/05','female','nourmohamed','522004');

select post_id, username from users
inner join posts on users.user_id = posts.user_id where post_id = 1;

/*inserting data for users*/
insert into users(username,password,first_name,last_name)
values('nour246','abc','nour','adel');

insert into users(username,password,first_name,last_name)
values('jana123','xyz','jana','mohamed');

insert into users(username,password,first_name,last_name)
values('ranwa34','qwe','ranwa','khaled');

insert into users(username,password,first_name,last_name)
values('nour908','poi','nour2','mohamed');

insert into users(username,password,first_name,last_name)
values('yasso_09','wwww','yasmine','ahmed');

insert into users(username,password,first_name,last_name)
values('xxxx_n','red123','aly','mohamed');

insert into users(username,password,first_name,last_name)
values('yahya005','2005','yahya','nael');

insert into users(username,password,first_name,last_name)
values('fifoo','faridaaaa','farida','ramy');

insert into users(username,password,first_name,last_name)
values('omar987','O2020','omar','nader');

insert into users(username,password,first_name,last_name)
values('lillyyy','lil','lily','hassan');
select * from users;

/*inserting data for messages*/
insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('hey','1999-7-14 2:35:13',1,5);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('love you ','2023-8-14 2:38:19',12,5);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('send this','2020-7-3 2:58:00',6,3);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('hello','1997-12-23 12:00:25',9,1);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('no comment','2022-8-9 2:35:13',8,1);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('calling now','1999-7-14 4:56:58',3,1);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('hey!','2015-11-14 5:12:39',5,8);

insert into messages (m_content, m_timestamp, sender_id, receiver_id)
values('please','2004-6-21 9:35:53',1,4);

/* Updating user info*/
UPDATE `social_media`.`users` SET `nbr_of_friends` = '5', `nbr_of_posts` = '3' WHERE (`user_id` = '4');
UPDATE `social_media`.`users` SET `first_name` = 'Oscar', `last_name` = 'fathy', `email` = 'oscar@gmail.com', `birthdate` = '2000-04-02', `gender` = 'female', `nbr_of_friends` = '12', `nbr_of_posts` = '4', `phonenumber` = '01928462' WHERE (`user_id` = '5');
UPDATE `social_media`.`users` SET `email` = 'samwilson987@icloud.com', `gender` = 'male', `nbr_of_friends` = '23', `phonenumber` = '02871573' WHERE (`user_id` = '13');
UPDATE `social_media`.`users` SET `email` = 'lisaanderson654@yahoo.com', `gender` = 'female', `nbr_of_friends` = '1', `phonenumber` = '9763452' WHERE (`user_id` = '14');
UPDATE `social_media`.`users` SET `email` = 'davidbrown321@outlook.com', `gender` = 'male', `nbr_of_friends` = '1', `phonenumber` = '0125362' WHERE (`user_id` = '11');
UPDATE `social_media`.`users` SET `email` = 'rachelgreen567@aol.com', `gender` = 'femle', `nbr_of_friends` = '6', `phonenumber` = '09271653' WHERE (`user_id` = '12');
UPDATE `social_media`.`users` SET `email` = 'john.doe456@hotmail.com', `gender` = 'male', `nbr_of_friends` = '3', `phonenumber` = '0918273' WHERE (`user_id` = '10');
UPDATE `social_media`.`users` SET `email` = 'emilyjones789@gmail.com', `gender` = 'female', `nbr_of_friends` = '5', `phonenumber` = '673811' WHERE (`user_id` = '9');
UPDATE `social_media`.`users` SET `email` = 'sarahsmith123@email.com', `gender` = 'female', `nbr_of_friends` = '4', `phonenumber` = '839201' WHERE (`user_id` = '8');
DELETE FROM `social_media`.`users` WHERE (`user_id` = '7');
UPDATE `social_media`.`users` SET `first_name` = 'Karim', `email` = 'karim@gmail.com', `gender` = 'male', `nbr_of_friends` = '2', `phonenumber` = '028472919' WHERE (`user_id` = '6');

INSERT INTO `social_media`.`messages` (`m_content`, `m_timestamp`, `receiver_id`, `sender_id`) VALUES ('how is the fam? ', '2023-12-23 12:22:34', '6', '5');
INSERT INTO `social_media`.`messages` (`message_id`, `m_content`, `m_timestamp`, `receiver_id`, `sender_id`) VALUES ('10', 'are you doing ok?', '2023-08-04 04:30:12', '5', '3');

SELECT users.username AS sender_username, messages.m_content, messages.m_timestamp, receiver.username AS receiver_username
FROM messages
INNER JOIN users ON messages.sender_id = users.user_id
INNER JOIN users AS receiver ON messages.receiver_id = receiver.user_id
WHERE receiver.username = 'ranwakhaled';

select* from users;
select* from messages;
select* from posts;
select* from comments;



