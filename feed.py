from random import randint
import customtkinter
import tkinter
import mysql.connector

# colors 
light_blue = '#c3e2ff'
royal_blue ='#121c86'
red='#d30e0e'
blue_grayish ='#dddddd'
# post id variables to use later when writing comments
post1_id = 0
post2_id = 0
# userid var to use it to go back to profile
user_name_owner = 0
# connecting to mysql
# open connection with database
myDB = mysql.connector.connect(host='localhost', user='root', password='ranwakhaled12',database='social_media')
mycursor = myDB.cursor()
# use the databse
command = 'use social_media'
mycursor.execute(command)

def display_info(userid):
    # initialize global userid 
    global user_name_owner
    user_name_owner=userid
    # retrieve the data from posts table in mysql 
    command = 'SELECT post_id,content, nbr_of_likes, nbr_of_shares, nbr_of_comments, timestamp FROM posts'
    mycursor.execute(command)
    # retrieve the data and store it in a variable
    post_data = mycursor.fetchall()  # an array of tuples - each tuple represents a row 
    # set the labels according to the retreived data
    # choose a random post to display from the table
    # initialize the post index
    post1_index = randint(0,len(post_data)//2)
    post2_index = randint(len(post_data)//2 +1, len(post_data)-1)
    print(post1_index, post2_index)
    # initialize post id
    global post1_id, post2_id
    post1_id=post_data[post1_index][0]
    post2_id=post_data[post2_index][0]
    print(post1_id, post2_id)
    # Post1: 
    # set the username of the post author 
    # Perfom inner join on the table
    command = 'SELECT post_id, username FROM users INNER JOIN posts ON users.user_id = posts.user_id WHERE post_id = %s'
    mycursor.execute(command, (post1_id,))
    user = mycursor.fetchone()
    print(user)
    username1.configure(text= user[1])
    # set the timestamp for the post 
    timestamp1.configure(text=post_data[post1_index][5])
    # set the content of the post 
    post_content1.configure(text=post_data[post1_index][1])
    # set the nbr of likes,shares & comments
    likes1.configure(text=f'Likes: {post_data[post1_index][2]}')
    shares1.configure(text=f'Shares: {post_data[post1_index][3]}')
    comments1.configure(text= f'Comments: {post_data[post1_index][4]}')

    # Post2: 
    # set the username of the post author 
    # Perfom inner join on the table
    command = 'SELECT post_id, username FROM users INNER JOIN posts ON users.user_id = posts.user_id WHERE post_id = %s'
    mycursor.execute(command, (post2_id,))
    user = mycursor.fetchone()
    print(user)
    username2.configure(text= user[1])
    # set the timestamp for the post 
    timestamp2.configure(text=post_data[post2_index][5])
    # set the content of the post 
    post_content2.configure(text=post_data[post2_index][1])
    # set the nbr of likes,shares & comments
    likes2.configure(text=f'Likes: {post_data[post2_index][2]}')
    shares2.configure(text=f'Shares: {post_data[post2_index][3]}')
    comments2.configure(text= f'Comments: {post_data[post2_index][4]}')

    # open the window
    feed_window.mainloop()

# functions
# function to be executed upon pressing the profile button
def go_to_messages():
    print(user_name_owner)
    feed_window.destroy()  # closing the eed 
    # opening the messages page
    from messagespage import show_messages
    show_messages(user_name_owner)
    
    
# function to be executed when we click publish button (to post the comment)
def publish_comment1():
    # get user id of the author of the comment 
    command = 'SELECT user_id FROM users where username = %s'
    mycursor.execute(command, (user_name_owner,))
    author_id = mycursor.fetchone()[0]
    # write the new post in the database 
    command = 'INSERT INTO comments (content, user_id, post_id) values (%s,%s,%s)'
    mycursor.execute(command, (comment_box1.get('0.0','end'), author_id, post1_id))
    # commit the changes to the database
    myDB.commit()
def publish_comment2():
    # get user id of the author of the comment 
    command = 'SELECT user_id FROM users where username = %s'
    mycursor.execute(command, (user_name_owner,))
    author_id = mycursor.fetchone()[0]
    # write the new post in the database 
    command = 'INSERT INTO comments (content, user_id) values (%s,%s,%s)'
    mycursor.execute(command, (comment_box2.get('0.0','end'),author_id, post2_id))
    # commit the changes to the database
    myDB.commit()

# Creating the window 
feed_window= customtkinter.CTk()
feed_window.geometry('700x700')  # setting the dimensions
feed_window.title('feed page')  # setting the title
feed_window.config(bg=blue_grayish)  # setting the background color

# create the frame to contain the 1st post
frame1 = customtkinter.CTkFrame(master=feed_window,
                                width= 650,
                                height=300,
                                corner_radius= 10,
                                bg_color=blue_grayish,
                                fg_color=light_blue)
frame1.place(relx=0.5,rely=0.3, anchor=tkinter.CENTER)

# a label for the username- the person who wrote the post 
username1 = customtkinter.CTkLabel(master=frame1,
                                      text_color= royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
username1.place(relx=0.1, rely=0.05)
# a label for the timestamp- the time the post was published 
timestamp1 = customtkinter.CTkLabel(master=frame1,
                                      text_color= royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
timestamp1.place(relx=0.3, rely=0.05)
# a prompt for the user to leave a commentt 
comment_prompt1 = customtkinter.CTkLabel(master=frame1,
                                         text='Leave a comment:',
                                         text_color= red,
                                         font=('times new roman', 18, 'bold'),
                                         bg_color=light_blue)
comment_prompt1.place(relx=0.6, rely=0.05)
# textbox to leave a comment 
comment_box1= customtkinter.CTkTextbox(master=frame1,
                                      bg_color=light_blue)
comment_box1.insert('0.0',"write comment.")
comment_box1.place(relx=0.6, rely=0.15)
# button to post the comment
comment_button1=customtkinter.CTkButton(master=frame1,
                                        width=70,
                                        height=35,
                                        text='publish',
                                        fg_color=red,
                                        font= ('Times new roman', 15,'bold'),
                                        text_color='#fff',
                                        command=publish_comment1)
comment_button1.place(relx=0.6,rely=0.85)
# label to show the post content
post_content1 = customtkinter.CTkLabel(master=frame1,
                                      text_color= 'black',
                                      wraplength= 200,
                                      font=('times new roman', 25),
                                      bg_color=light_blue)
post_content1.place(relx=0.1, rely=0.3)
# labels to show the nbr of likes, shares & comments
likes1 =  customtkinter.CTkLabel(master=frame1,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
likes1.place(relx=0.1,rely= 0.85)
shares1= customtkinter.CTkLabel(master=frame1,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
shares1.place(relx=0.25,rely= 0.85)
comments1=customtkinter.CTkLabel(master=frame1,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
comments1.place(relx=0.4,rely= 0.85)

# create the frame to contain the 2nd post
frame2 = customtkinter.CTkFrame(master=feed_window,
                                width= 650,
                                height=300,
                                corner_radius= 10,
                                bg_color=blue_grayish,
                                fg_color=light_blue)
frame2.place(relx=0.5,rely=0.75, anchor=tkinter.CENTER)

# a label for the username- the person who wrote the post 
username2 = customtkinter.CTkLabel(master=frame2,
                                      text_color= royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
username2.place(relx=0.1, rely=0.05)
# a label for the timestamp- the time the post was published 
timestamp2 = customtkinter.CTkLabel(master=frame2,
                                      text_color= royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
timestamp2.place(relx=0.3, rely=0.05)
# a prompt for the user to leave a commentt 
comment_prompt2 = customtkinter.CTkLabel(master=frame2,
                                         text='Leave a comment:',
                                         text_color= red,
                                         font=('times new roman', 18, 'bold'),
                                         bg_color=light_blue)
comment_prompt2.place(relx=0.6, rely=0.05)
# textbox to leave a comment 
comment_box2= customtkinter.CTkTextbox(master=frame2,
                                      bg_color=light_blue)
comment_box2.insert('0.0',"write comment.")
comment_box2.place(relx=0.6, rely=0.15)
# button to post the comment
comment_button2=customtkinter.CTkButton(master=frame2,
                                        width=70,
                                        height=35,
                                        text='publish',
                                        fg_color=red,
                                        font= ('Times new roman', 15,'bold'),
                                        text_color='#fff',
                                        command=publish_comment2)
comment_button2.place(relx=0.6,rely=0.85)
# label to show the post content
post_content2 = customtkinter.CTkLabel(master=frame2,
                                      text_color= 'black',
                                      wraplength=200,
                                      font=('times new roman', 25),
                                      bg_color=light_blue)
post_content2.place(relx=0.1, rely=0.3)
# labels to show the nbr of likes, shares & comments
likes2 =  customtkinter.CTkLabel(master=frame2,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
likes2.place(relx=0.1,rely= 0.85)
shares2= customtkinter.CTkLabel(master=frame2,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
shares2.place(relx=0.25,rely= 0.85)
comments2=customtkinter.CTkLabel(master=frame2,
                                      text_color= royal_blue,
                                      font=('times new roman', 14, 'bold'),
                                      bg_color=light_blue)
comments2.place(relx=0.4,rely= 0.85)



# creating the profile button - to take tothe user to the profile info page 
profile = customtkinter.CTkButton(master=feed_window,
                                  width=70,
                                  height=40,
                                  fg_color=red,
                                  text='Inbox',
                                  font=('Times new roman', 15,'bold'),
                                  text_color='#fff',
                                  command=go_to_messages)
profile.place(relx=0.02, rely=0.02)


