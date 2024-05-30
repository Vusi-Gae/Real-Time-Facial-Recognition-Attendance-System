import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattedancerealtimetshepang-default-rtdb.firebaseio.com/"
})


ref = db.reference('students')

data = {
    "754321":
        {
            "name": "Tshepang Gaeatlholwe",
            "major": "Geoinformatics",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-05-29 00:54:34"
        },
    "654321":
    {
            "name": "Ernest Mokoena",
            "major": "Geology",
            "starting_year": 2024,
            "total_attendance": 15,
            "standing": "VG",
            "year": 4,
            "last_attendance_time": "2024-05-29 00:54:34"
        }
    }

for key,value in data.items():
    ref.child(key).set(value)
