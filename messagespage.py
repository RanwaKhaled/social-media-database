import customtkinter
import tkinter
import mysql.connector
from tkinter import ttk

message_data=None
#connecting to mysql
#open connection with database
myDB = mysql.connector.connect(host='localhost',user='root',password='ranwakhaled12',database='social_media')
mycursor = myDB.cursor()
#use database
command = 'use social_media'
mycursor.execute(command)

def show_messages(user_name):
    global message_data

    # Create a Treeview 
    columns = ('Sender username',"Message", "Timestamp")
    treeview = ttk.Treeview(master=message, columns=columns, show="headings",height=13)

    # styling the fonts and labels
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Times new roman', 20,'bold'), foreground=royal_blue)
    style.configure("Treeview",font=(None,18,), padding=(10, 10),rowheight=40)

    # adjusting the dimensions of the columns
    treeview.column("Message",stretch=True,width=300)
    treeview.column("Timestamp",stretch=True,width=300)
    treeview.column("Sender username",stretch=True,width=300)

    # Add column headings
    for col in columns:
        treeview.heading(col, text=col)

    #retrieve data from messages table in mysql
    command = '''
        SELECT users.username AS sender_username, messages.m_content, messages.m_timestamp, receiver.username AS receiver_username
        FROM messages
        INNER JOIN users ON messages.sender_id = users.user_id
        INNER JOIN users AS receiver ON messages.receiver_id = receiver.user_id
        WHERE receiver.username = %s;
    '''
    mycursor.execute(command, (user_name,))
    #retrieve the data and store it in a variable
    message_data = mycursor.fetchall() # an array of tuples. each tuple represents a row

    # Insert data into the Treeview
    for row in message_data:
        treeview.insert("", tkinter.END, values=row)

    treeview.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    message.mainloop()



#set colors 
light_blue = '#c3e2ff'
royal_blue ='#121c86'
red='#d30e0e'
blue_grayish ='#dddddd'

message = customtkinter.CTk()

message.config(bg=light_blue)

message.title("Message viewer")
message.geometry("900x700")


label = customtkinter.CTkLabel(master=message,
                               text="Incoming messages",
                               width=125,
                               height=30,
                               font=("Times new roman", 45,'bold'),
                               fg_color=light_blue,
                               bg_color=light_blue,
                               text_color = red,
                               corner_radius=8)

label.grid(padx=20,pady=20)
label.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)

show_messages('ranwakhaled')