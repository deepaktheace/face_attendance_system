import tkinter
import customtkinter
from PIL import ImageTk, Image
customtkinter.set_appearance_mode("dark") #can set light or dark.
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green
app=customtkinter.CTk() #creating custom tkinter window
app.geometry("1280x720")
app.title('Attendance System - Login')
img1=ImageTk.PhotoImage (Image.open("Resources/pattern.png"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()

frame=customtkinter.CTkFrame (master=l1, width=320, height=360)
frame.place(relx=0.5, rely=0.5, anchor= tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

#Creating custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=210)

l3=customtkinter.CTkLabel(master=frame, text="Contact Owner",font=('Century Gothic',14))
l3.place(x=50,y=250)

img2=customtkinter.CTkImage(Image.open("Resources/Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("Resources/124010.png").resize((20,20), Image.ANTIALIAS))
button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)


app.mainloop()