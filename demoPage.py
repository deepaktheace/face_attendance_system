import customtkinter 
import tkinter as tk 
#from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from tkinter import *
from firebase_admin import credentials,db,initialize_app
import firebase_admin
import json
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
        "234910":{
        "name":"Raj Shah demo",
        "stream":"ANDROID",
        "starting_year":"2020",
        "total_attendance":"15",
        "div":"A",
        "year":"2nd",
        "last_attendance_time":"2023-02-25 00:54:23",
    }
}

for key, value in data.items():
    ref.child(key).set(value)

