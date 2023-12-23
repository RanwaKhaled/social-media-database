import customtkinter
import tkinter
import mysql.connector
import time 

# colors 
light_blue = '#c3e2ff'
royal_blue ='#121c86'
red='#d30e0e'
blue_grayish ='#dddddd'

gender_choice=''  #to store the value of gender chosen
# functions
def open_signup():
    signUp_window.mainloop()
def close_signup():
    signUp_window.destroy()
# function to get the gender selected
def get_gender(choice):
    global gender_choice
    gender_choice = choice  # return string: male or female
# function to enter the user data in the database and reopen login
def signup():
    # open the connection with the database 
    myDB = mysql.connector.connect(host='localhost', user='root', password='ranwakhaled12',database='social_media')
    mycursor = myDB.cursor()
    print('connected to database')
    # Use the database
    command = 'use social_media'
    mycursor.execute(command)
    # enter the data in the database   
    command = 'INSERT INTO users (username, password, first_name,last_name,email,phonenumber,birthdate,gender) values (%s,%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(command,(user.get(),password.get(),fname.get(),lname.get(),email.get(),phone.get(),dateoB.get(),gender_choice))
    # commit changes to database
    myDB.commit()
    # close the sign up window
    close_signup()
    # reopen login window to log in eith newly created account
    from loginpage import window
    window.mainloop()
    

# create window
signUp_window = customtkinter.CTk()  # creating the window
signUp_window.geometry('600x600')  # setting the size
signUp_window.title('Sign up')  # setting the title
signUp_window.config(bg=royal_blue)

# adding a title to the frame 
sign_in_title = customtkinter.CTkLabel(master=signUp_window,
                                      text='Sign up',
                                      text_color='white',
                                      font=('Times new roman', 45,'bold'),
                                      bg_color=royal_blue)
sign_in_title.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

# first name entry prompt 
# creating the prompt 
fname_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='First Name:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
fname_prompt.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)

# creating an entry textbox 
fname = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter first name',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the first name entry
fname.place(relx=0.65, rely=0.15, anchor=tkinter.CENTER)

# last name entry prompt 
# creating the prompt 
lname_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Last Name:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
lname_prompt.place(relx=0.3, rely=0.25, anchor=tkinter.CENTER)

# creating an entry textbox 
lname = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter last name',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the first name entry
lname.place(relx=0.65, rely=0.25, anchor=tkinter.CENTER)

# email entry prompt 
# creating the prompt 
email_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Email:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
email_prompt.place(relx=0.3, rely=0.35, anchor=tkinter.CENTER)

# create an entry for email
email = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter user email',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the email entry
email.place(relx=0.65, rely=0.35, anchor=tkinter.CENTER)

# phone number entry prompt 
# creating the prompt 
phone_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Phone number:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
phone_prompt.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

# create an entry for phone number
phone = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter phone number',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the email entry
phone.place(relx=0.65, rely=0.45, anchor=tkinter.CENTER)

# create an entry for the date of birth
dateoB = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='YYYY-MM-DD',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the date of birth entry
dateoB.place(relx=0.65, rely=0.55, anchor=tkinter.CENTER)

# date of birth entry prompt 
# creating the prompt 
dateoB_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Date of Birth:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
dateoB_prompt.place(relx=0.3, rely=0.55, anchor=tkinter.CENTER)

# create a menu for gender
# set initial value
gender_var = customtkinter.StringVar(value='gender')
# creating option menu
gender = customtkinter.CTkOptionMenu(master=signUp_window,
                                    values=['male', 'female'],
                                    bg_color=royal_blue,
                                    fg_color='white',
                                    variable=gender_var,
                                    command= get_gender)
# set font color 
gender.configure(text_color='black')
# place the gender entry
gender.place(relx=0.65, rely=0.65, anchor=tkinter.CENTER)

# Gender entry prompt 
# creating the prompt 
gender_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Gender:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
gender_prompt.place(relx=0.3, rely=0.65, anchor=tkinter.CENTER)

# creating an entry textbox 
user = customtkinter.CTkEntry(master=signUp_window,  # put it in the frame
                              width=200,  # set the width
                              height=40,
                              fg_color= '#fff',  #foreground(aka font color): black
                              placeholder_text='enter user name',
                              bg_color=royal_blue,  # set the background color
                              font=('Times new roman', 16))  # setting the font style and size
# place the username entry
user.place(relx=0.65, rely=0.75, anchor=tkinter.CENTER)

# User entry prompt 
# creating the prompt 
user_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Username:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
user_prompt.place(relx=0.3, rely=0.75, anchor=tkinter.CENTER)

# create a password entry - to enter the password
password = customtkinter.CTkEntry(master=signUp_window,
                                  width=200,
                                  height=40,
                                  fg_color= '#fff',  #foreground(aka font color): black
                                  placeholder_text='enter password',
                                  bg_color=royal_blue,  # set the background color
                                  font=('Times new roman', 16),  # setting the font style and size)
                                  show='*')
# place the password entry
password.place(relx=0.65, rely=0.85, anchor=tkinter.CENTER)

# password entry prompt 
# creating the prompt 
password_prompt = customtkinter.CTkLabel(master=signUp_window,
                                     text='Password:',
                                     bg_color=royal_blue,
                                     text_color='white',
                                     font=('Times new roman', 18, 'bold'))
# placing the prompt 
password_prompt.place(relx=0.3, rely=0.85, anchor=tkinter.CENTER)

# Create the buttons
# Create the sign up buttons 
sign_up = customtkinter.CTkButton(master=signUp_window,
                               width= 70,
                               height=35,
                               fg_color= red,
                               text='Sign up',
                               text_color='#fff',
                               font=('Arial',16,'bold'),
                               bg_color=royal_blue,
                               command=signup)
sign_up.place(relx=0.55, rely = 0.93, anchor=tkinter.CENTER)

