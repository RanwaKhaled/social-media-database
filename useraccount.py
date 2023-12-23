import os
import customtkinter
import tkinter
from PIL import Image
import mysql.connector
import time 

# colors 
light_blue = '#c3e2ff'
royal_blue ='#121c86'
red='#d30e0e'
blue_grayish ='#dddddd'

# connecting to mysql
# open connection with database
myDB = mysql.connector.connect(host='localhost', user='root', password='ranwakhaled12',database='social_media')
mycursor = myDB.cursor()
# use the databse
command = 'use social_media'
mycursor.execute(command)
# defining user id
userid=0
# defining global username to use for the feed 
user_name=''

# functions
# function to display the user info in their specified labels
def display_info(user_id):
    global user_name
    user_name = user_id
    print(user_id)
    # retrieve info from the database
    command='SELECT* FROM users WHERE username =%s'
    mycursor.execute(command,(user_id,))
    # store retreived info in a variable - type: tuple
    myresult=mycursor.fetchone()
    print(myresult)

    # use the retreived data to display the account details
    # add the data to the labels
    username.configure(text=myresult[1])
    fname.configure(text=myresult[3])
    lname.configure(text=myresult[4])
    email.configure(text=myresult[5])
    birthdate.configure(text=myresult[6])
    phone.configure(text=myresult[10])
    
    # initialize user id with the retrieved data
    global userid
    userid=myresult[0]
    # open window
    account_window.mainloop()

# function to return what is written in the post text box content
def post_content():
    return new_post_content.get('0.0','end')
# function to be executed upon clicking the button 'new post'
def postB_click():
    # command to insert new post in table 
    command='INSERT INTO posts (content, user_id) values (%s,%s)'
    mycursor.execute(command,(post_content(), userid))
    # commit changes to the table
    myDB.commit()
    # reset textbox
    new_post_content.delete('0.0','end')
    # rewrite default value 
    new_post_content.insert('0.0',"what's on your mind?")

# function to call upon clicking the button 'edit'
def edit_click():  # we will see the changes upon reopenening the account
    # ask for the field that he wants to edit
    edit_q = customtkinter.CTkInputDialog(text='what do you want to edit?', title='edit')
    col=edit_q.get_input()
    print(col)
    if col:
        # get the new value to update
        value_q = customtkinter.CTkInputDialog(text='enter new value', title='edit')
        value = value_q.get_input()
        # update the new value in the sql db
        command = 'UPDATE users SET {} = %s WHERE user_id = %s'.format(col)
        mycursor.execute(command, (value,userid))
        # commit changes to the database
        myDB.commit()
# function to be executed upon clicking the button 'home'
def home_click():
    global user_name
    account_window.destroy()
    from feed import display_info
    display_info(user_name)

    


# creating the account window
account_window = customtkinter.CTk()  # creating the window
account_window.geometry('700x750')  # setting the size
account_window.title('user account')  # setting the title 
account_window.config(bg=light_blue)  # setting the bckground color

# the top part of the page 
# create a frame to contain that 
top_frame = customtkinter.CTkFrame(master=account_window,
                                   width=700,
                                   height=200,
                                   corner_radius=20,  # how rounded the corners will be 
                                   bg_color=light_blue,
                                   fg_color=light_blue)
top_frame.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)
# Home button - a button that takes me to the feed where the posts are 
home = customtkinter.CTkButton(master=top_frame,
                               width= 70,
                               height=40,
                               fg_color= red,
                               text='Home',
                               font=('Times new roman', 15,'bold'),
                               text_color='#fff',
                               command=home_click)
home.place(relx=0.01, rely=0.1)
"""# Profile icon
# load the image for the female
female_icon=customtkinter.CTkImage(light_image=Image.open(os.path.join('D:/Uni stuff/2nd year/1st semester/Introduction to databases/Project/female icon.png')),size=(150,150))
# create a label to display the image into
pp_label = customtkinter.CTkLabel(master=top_frame, text='')
pp_label.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
pp_label.configure(image = female_icon)"""


# the middle part of the page - the one containing the account info
middle_frame=customtkinter.CTkFrame(master=account_window,
                                   width=700,
                                   height=500,
                                   corner_radius=20,  # how rounded the corners will be 
                                   bg_color=light_blue,
                                   fg_color= light_blue)
middle_frame.place(relx=0.5, rely=0.55,anchor=tkinter.CENTER)
# Add area to write new posts
# prompt to write new post 
new_post_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Write new post:',
                                      text_color= red,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
new_post_prompt.place(relx=0.65, rely= 0.2, anchor=tkinter.CENTER)
# add textbox to add the post content
new_post_content = customtkinter.CTkTextbox(master=middle_frame,
                                            bg_color=light_blue,
                                            )
new_post_content.insert('0.0',"what's on your mind?")
new_post_content.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
# add labels for user data to be displayed  
# first name prompt 
fname_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='First name:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
fname_prompt.place(relx=0.2, rely= 0.2, anchor=tkinter.CENTER)
# first name user data 
fname = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
fname.place(relx=0.35, rely= 0.2, anchor=tkinter.CENTER)
# last name prompt 
lname_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Last name:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
lname_prompt.place(relx=0.2, rely= 0.3, anchor=tkinter.CENTER)
# last name user data 
lname = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
lname.place(relx=0.35, rely= 0.3, anchor=tkinter.CENTER)
# username prompt 
username_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Username:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
username_prompt.place(relx=0.2, rely= 0.4, anchor=tkinter.CENTER)
# username user data 
username = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
username.place(relx=0.35, rely= 0.4, anchor=tkinter.CENTER)
# date of birth prompt 
dob_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Date of birth:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
dob_prompt.place(relx=0.2, rely= 0.5, anchor=tkinter.CENTER)
# date of birth user data 
birthdate = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
birthdate.place(relx=0.35, rely= 0.5, anchor=tkinter.CENTER)
# phone number prompt 
phone_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Phone number:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
phone_prompt.place(relx=0.2, rely= 0.6, anchor=tkinter.CENTER)
# phone number user data 
phone = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
phone.place(relx=0.37, rely= 0.6, anchor=tkinter.CENTER)
# email prompt 
email_prompt = customtkinter.CTkLabel(master=middle_frame,
                                      text='Email:',
                                      text_color=royal_blue,
                                      font=('times new roman', 18, 'bold'),
                                      bg_color=light_blue)
email_prompt.place(relx=0.16, rely= 0.7, anchor=tkinter.CENTER)
# email user data 
email = customtkinter.CTkLabel(master=middle_frame,
                                text_color=royal_blue,
                                font=('times new roman', 18, 'bold'),
                                bg_color=light_blue)
email.place(relx=0.35, rely= 0.7, anchor=tkinter.CENTER)

# create frame to contain the bottom part of the page 
bottom_frame = customtkinter.CTkFrame(master=account_window,
                                   width=700,
                                   height=100,
                                   corner_radius=20,  # how rounded the corners will be 
                                   bg_color=light_blue,
                                   fg_color=light_blue)
bottom_frame.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
# create a button to edit the account info
edit = customtkinter.CTkButton(master=bottom_frame,
                               width= 70,
                               height=40,
                               fg_color= red,
                               text='Edit',
                               font=('Times new roman', 25,'bold'),
                               text_color='#fff',
                               command=edit_click)
edit.place(relx=0.65, rely=0.3, anchor=tkinter.CENTER)
# create a button to create a new post
post = customtkinter.CTkButton(master=bottom_frame,
                               width= 70,
                               height=40,
                               fg_color= red,
                               text='New Post',
                               font=('Times new roman', 25,'bold'),
                               text_color='#fff',
                               command=postB_click)
post.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)
