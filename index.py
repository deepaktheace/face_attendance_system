import face_recognition
import os 
import cv2 as cv 
import numpy as np
import pickle
from cvzone import cornerRect
import firebase_admin
from firebase_admin import credentials,db,storage
from time import sleep
from datetime import datetime
from subprocess import Popen

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/",
    'storageBucket':'realtimefaceattendance-53e9b.appspot.com',
})
bucket = storage.bucket()

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
print(cap.read())
sleep(7)

background = cv.imread('Resources/background.png')

def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv.resize(image, dim, interpolation=inter)

#importing images 
modeFolderPath = 'Resources/Modes'
modePathList = os.listdir(modeFolderPath)
modeList = []
for path in modePathList:
    modeList.append(cv.imread(os.path.join(modeFolderPath,path)))

#importing Encoded files
file  = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown,studentIds = encodeListKnownWithIds
modeType = 0
counter = 0
id = 0
imgStudent = []

#reading Camera Data
while True:
    success, img = cap.read()
    #image reading
    #imgS = maintain_aspect_ratio_resize(img,216,216)
    imgS = cv.resize(img,(0, 0),None,0.25,0.25)
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    #setting up background
    background[162:162+480,55:55+640] = img
    background[44:44+633,808:808+414] = modeList[modeType]
    
    if faceCurFrame:
        for encodeFace, FaceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            y1, x2, y2, x1 = FaceLoc
            y1, x2, y2, x1 = y1*4 , x2*4, y2*4, x1*4
            bbox = 55+x1, 162+y1, x2-x1, y2-y1 
            background = cornerRect(background,bbox, rt=0)
            matchIndex =  np.argmin(faceDis) if np.argmin(faceDis) < 0.5 else 1
            if matches[matchIndex] != True:
                print("Unknown Face Detected")
            if matches[matchIndex]:
                id = studentIds[matchIndex]
                print(id)
                if counter == 0: 
                    counter = 1
        if counter!= 0:
            # Getting Data
            if counter == 1:
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo) 
                blob = bucket.get_blob(f'Images/{id}.png')
                if blob != None:
                    array = np.frombuffer(blob.download_as_string(),np.uint8)
                    imgStudent = cv.imdecode(array,cv.COLOR_BGRA2BGR)
                    imgStudent = maintain_aspect_ratio_resize(imgStudent,216,216)
                    #update data
                    dateTimeObject = datetime.strptime(studentInfo['last_attendance_time'],"%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now()-dateTimeObject).total_seconds()
                    if secondsElapsed >= 60:                                
                        ref = db.reference(f'Students/{id}')
                        studentInfo['total_attendance'] = int(studentInfo['total_attendance'])
                        studentInfo['total_attendance'] += 1
                        ref.child('total_attendance').set(studentInfo['total_attendance'])
                        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        cmd = "python update.py"
                        p = Popen(cmd, shell=True)
                    else:
                        modeType = 3
                        counter = 0
                        background[44:44+633,808:808+414] = modeList[modeType]

            if modeType != 3:
                if 30<counter<40:
                    modeType = 2
                    background[44:44+633,808:808+414] = modeList[modeType]

                if 10<counter<30:   
                    modeType = 1
                    cv.putText(background,str(studentInfo['total_attendance']),(861,125),
                            cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                    cv.putText(background,str(studentInfo['stream']),(1006,550),
                            cv.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv.putText(background,str(id),(1006,493),
                            cv.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv.putText(background,str(studentInfo['div']),(910,625),
                            cv.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    cv.putText(background,str(studentInfo['year']),(1025,625),
                            cv.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    cv.putText(background,str(studentInfo['starting_year']),(1125,625),
                            cv.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)

                    (w, h), _ = cv.getTextSize(studentInfo['name'], cv.FONT_HERSHEY_COMPLEX,1,1)
                    offset  = (414 - w)//2
                    cv.putText(background,str(studentInfo['name']),(808+offset,445),
                            cv.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
                    background[175:175+216,909:909+216] = imgStudent
            
                counter+=1

                if counter>36:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    background[44:44+633,808:808+414] = modeList[modeType]
    else:
        modeType = 0
        counter = 0        

    cv.imshow("Taking Attendance",background)
    if cv.waitKey(1) == ord('q'):
        break
    