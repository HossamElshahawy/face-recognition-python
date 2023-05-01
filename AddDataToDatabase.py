import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-b544e-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-b544e.appspot.com"
})


ref = db.reference('Students')

data = {
    "963852": {
        "name": "elon mask",
        "major": "Bio",
        "starting_year": 2018,
        "total_attendance": 6,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-5 00:54:34"
    },
"852741": {
        "name": "emely",
        "major": "cs",
        "starting_year": 2019,
        "total_attendance": 5,
        "standing": "B",
        "year": 2,
        "last_attendance_time": "2022-12-5 00:54:33"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
