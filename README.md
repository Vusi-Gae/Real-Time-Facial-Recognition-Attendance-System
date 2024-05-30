Real-Time Facial Recognition Attendance System\
Project Overview\
This project aims to automate and streamline the process of tracking student attendance using real-time facial recognition technology. The system leverages computer vision and machine learning to accurately identify students and record their attendance, providing a more efficient and reliable alternative to traditional attendance methods.\

Team Members\
Tshepang Gaeatlholwe (Team Lead)\
Ernest Mokoena (Lead Developer\

System Architecture
The system architecture comprises several key components:
Webcam: Captures real-time video frames.
OpenCV: Used for image processing and capturing frames from the webcam
face_recognition Library: Facilitates face detection and encoding.
Firebase: Backend for storing student information, attendance records, and facial images.
Firebase Realtime Database: For storing data records.
Firebase Storage: For storing image files.
cvzone: Enhances the display of bounding boxes and other UI elements on the images.
pickle: Used for serializing and deserializing facial encodings and student IDs.

Technologies Used
OpenCV: For image processing and frame capture.
face_recognition Library: For face detection and encoding.
Firebase: For real-time database and storage solutions.
cvzone: For UI enhancements.
pickle: For data serialization.
Project Setup
Prerequisites
Python 3.x
pip (Python package installer)
Firebase account with a configured Realtime Database and Storage Bucket
Webcam

