import customtkinter
import tkinter
import mysql.connector
import time 
from signuppage import open_signup

# colors 
light_blue = '#c3e2ff'
royal_blue ='#121c86'
red='#d30e0e'
blue_grayish ='#dddddd'

user_id=''  # username
# defining the needed functions
def check_credentials():
    global user_id
    # get the username and passweord entered by the user 
    user_id = user.get()
    user_password= password.get()
    # connecting with the database
    myDB = mysql.connector.connect(host='localhost', user='root', password='ranwakhaled12',database='social_media')
    mycursor = myDB.cursor()
    print('connected to database')

    command = 'use social_media'
    mycursor.execute(command)
    command='select* from users where username=%s and password=%s'
    mycursor.execute(command,(user_id, user_password))
    myresult = mycursor.fetchone()
    print(myresult)
    user_id=myresult[1]

    if myresult != None:  # meaning that the data exists in the table
        log_in_msg.configure(text='connected successfully')
    else:
        log_in_msg.configure(text='please check username and password')
    

# a function to close the login window after log in is successful
def close_login():
    window.destroy()

# function to call when we press the log in button
def press_login():
    global user_id
    check_credentials()
    from useraccount import display_info
    display_info(user_id)
    

# function to call when we press the sign up button
def press_signup():
   close_login()
   open_signup()

# create window
window= customtkinter.CTk()  # creating the window
window.title('Log in page')  # setting the title
window.geometry('500x500')  # setting the dimensions
window.config(bg=light_blue)  # setting the background color

# create frame 
frame = customtkinter.CTkFrame(master=window,
                               width= 300,  # setting the width
                               height=300,  # setting the height
                               corner_radius=20,  # how rounded will the corners be
                               bg_color=light_blue,
                               fg_color=royal_blue)  
frame.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)  # setting the place of the frame

# adding a title to the frame 
log_in_title = customtkinter.CTkLabel(master=frame,
                                      text='Log in',
                                      text_color='white',
                                      font=('Times new roman', 45,'bold'),
                                      bg_color=royal_blue)
log_in_title.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# create a user entry - to enter the username 
user = customtkinter.CTkEntry(master=frame,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter user name',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size

# setting the location
user.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
# create a password entry - to enter the password
password = customtkinter.CTkEntry(master=frame,
                                  width=200,
                                  height=40,
                                  fg_color= '#fff',  #foreground(aka font color): black
                                  placeholder_text='enter password',
                                  bg_color=royal_blue,  # set the background color
                                  font=('Times new roman', 16),  # setting the font style and size)
                                  show='*')
# setting the location
password.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

# create the log in button
log_in=customtkinter.CTkButton(master=frame,
                               width= 70,
                               height=30,
                               fg_color= red,
                               text='Log in',
                               text_color='#fff',
                               command = press_login)
# setting the location of the button
log_in.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

# create the sign up button
sign_up=customtkinter.CTkButton(master=frame,
                               width= 70,
                               height=30,
                               fg_color= red,
                               text='Sign up',
                               text_color='#fff',
                               command= press_signup)
# setting the location of the button
sign_up.place(relx=0.55, rely=0.7, anchor=tkinter.CENTER)

# create the label where the message will appear
log_in_msg = customtkinter.CTkLabel(master=frame,
                                    text='',
                                    text_color='white',
                                    bg_color=royal_blue
                                    )
log_in_msg.place(relx=0.5,rely=0.85, anchor=tkinter.CENTER)

window.mainloop()