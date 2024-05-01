# Social Media Database 
The database was housed on the local host of `MySQL Workbench`<br>
This repository contains:
## **MySQL script:** 
containing the data & the tables of the database
### Database Entities:
* Users
* Comments
* Posts
* Reactions
* Messages <br>
### Business Rules:
- A user can have many posts, but a post must have one user. 
- A post can have many comments, but a comment must be posted on one post. 
- A post can have many reactions, but a reaction must be made on one post. 
- A user can post many comments, but a comment must be posted by one user. 
- A user can send many messages, and messages can be sent by many users.
### ERD 
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/2ba6f31c-1067-4989-9ea2-ce9a592cc9bc" width = 500>
<h3>Schema</h3> 
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/d50bf453-bc63-4a71-9844-79c106143f60" width=500>

## **Python GUI Files:** 
containing the GUI and linking it to the MySQL database<br>
Made using the `customtkinter` library in Python<br>
**N:B:** Begin by running the GUI from the <i>loginpage.py</i> file
<h4><u>Log in Page</u></h4>
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/4c7e4170-845a-4236-9163-2986aa928432" width=300> <br>
<h4><u>Sign up Page</u></h4>
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/b0023253-cc39-4df6-9d9d-70036e34687b" width=300>
<h4><u>User Account page</u></h4>
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/8ed66cbd-d18f-4b7b-a918-59b2b030951a" width=300>
<h4><u>Feed Page</u></h4>
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/ad5cca92-b295-4155-9af1-25b70657695f" width=300>
<h4><u>Incoming Messages Page</u></h4>
<img src="https://github.com/RanwaKhaled/social-media-database/assets/77844198/726d59aa-a4fe-4ec4-9455-a08d8545f6af" width=300>
