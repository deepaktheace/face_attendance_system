import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":{
        "name":"Emily Watson",
        "stream":".NET",
        "starting_year":"2020",
        "total_attendance":"6",
        "div":"B",
        "year":"3rd",
        "last_attendance_time":"2023-02-25 00:54:23",
    },
    "561234":{
        "name":"Elon Musk",
        "stream":".NET",
        "starting_year":"2021",
        "total_attendance":"10",
        "div":"A",
        "year":"2nd",
        "last_attendance_time":"2023-02-25 00:54:23",
    },
    "783523":{
        "name":"Mohit Garude",
        "stream":"WEB DEV",
        "starting_year":"2020",
        "total_attendance":"20",
        "div":"B",
        "year":"3rd",
        "last_attendance_time":"2023-02-25 00:54:23",
    },
    "100234":{
        "name":"Deepak Gupta",
        "stream":"A.I.",
        "starting_year":"2020",
        "total_attendance":"6",
        "div":"B",
        "year":"3rd",
        "last_attendance_time":"2023-02-25 00:54:23",
    }
}

for key, value in data.items():
    ref.child(key).set(value)