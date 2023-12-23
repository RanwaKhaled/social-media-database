import os
import customtkinter 
from PIL import Image
import tkinter

app = customtkinter.CTk()
gender='female'
# load the image for the female
female_icon=customtkinter.CTkImage(light_image=Image.open(os.path.join('female icon.png')),size=(150,150))
# load the image 
male_icon=customtkinter.CTkImage(light_image=Image.open(os.path.join('male icon.png')),size=(150,150))
# create a label to display the image into
pp_label = customtkinter.CTkLabel(master=app, text='')
pp_label.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

if gender == 'male':
    pp_label.configure(image = male_icon)
else:
    pp_label.configure(image = female_icon)

app.mainloop()
