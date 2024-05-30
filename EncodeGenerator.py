import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattedancerealtimetshepang-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattedancerealtimetshepang.appspot.com"
})

# Importing students' images
folderPath = 'Images'
PathList = os.listdir(folderPath)
print("PathList:", PathList)
imgList = []
studentsIDs = []

for path in PathList:
    img_path = f"{folderPath}/{path}"
    imgList.append(cv2.imread(img_path))
    studentsIDs.append(os.path.splitext(path)[0])

    bucket = storage.bucket()
    blob = bucket.blob(img_path)

    print(f"Preparing to upload file: {img_path}")

    # Open the file and pass the file object to upload_from_file
    try:
        with open(img_path, 'rb') as file:
            print(f"Uploading file: {img_path}")
            blob.upload_from_file(file)
            print(f"Uploaded file: {img_path}")
    except Exception as e:
        print(f"Error uploading file {img_path}: {e}")

print("studentsIDs:", studentsIDs)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encodings Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentsIDs]
print("Encodings Complete")

with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIDs, file)

print("File Saved")
