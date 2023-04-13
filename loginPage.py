from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
from functools import partial
from subprocess import Popen

customtkinter.set_appearance_mode("dark") #can set light or dark.
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green
app=customtkinter.CTk() #creating custom tkinter window
app.geometry("720x500")
app.title('Smart Attendance System - Login')
img1=ImageTk.PhotoImage (Image.open("Resources/pattern.png"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

def button_function(userName,password):
    print("username entered :", userName.get())
    print("password entered :", password.get())
    usrName =userName.get()
    passWord=password.get()
    if usrName == "admin" and passWord == "12345":
        cmd = "python crud/crud_system.py"
        p = Popen(cmd, shell=True)
        app.destroy()
    else:
        messagebox.showwarning("Warning", "Invalid Username or Password")

    return

frame=customtkinter.CTkFrame (master=l1, width=320, height=360)
frame.place(relx=0.5, rely=0.5, anchor= CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)
userName = StringVar()
password = StringVar()

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username', textvariable=userName)
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*", textvariable=password)
entry2.place(x=50, y=165)

l2=customtkinter.CTkLabel (master=frame, text="Forget password", font=('Century Gothic', 12))
l2.place(x=165,y=195)
button_function = partial(button_function, userName ,password)
#Creating custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

img2=customtkinter.CTkImage(Image.open("Resources/Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("Resources/124010.png").resize((20,20), Image.ANTIALIAS))
button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)


app.mainloop()