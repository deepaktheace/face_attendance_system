import customtkinter #pip install customtkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

app=customtkinter.CTk()
app.title("Employee System")
app.geometry("800x500")
app.config(bg="#17043d")

font1=('Arial',20, 'bold')
font2=('Arial',15, 'bold')
font3=('Arial', 12, 'bold')

frame1=customtkinter.CTkFrame (app, fg_color="#FFFFFF",width=450,height=500)
frame1.place(x=350, y=0)


app.mainloop()


'''
from firebase_admin import credentials,db,initialize_app

cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
        "234911":{
        "name":"Raj Shah",
        "stream":"ANDROID",
        "starting_year":"2020",
        "total_attendance":"15",
        "div":"A",
        "year":"2rd",
        "last_attendance_time":"2023-02-25 00:54:23",
    }
}

for key, value in data.items():
    ref.child(key).set(value)
'''
