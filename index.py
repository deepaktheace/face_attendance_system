import face_recognition
import os 
import cv2 as cv 
import numpy as np
import pickle

background = cv.imread('Resources/background.png')

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

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
print(studentIds)


#reading Camera Data
while True:
    success, img = cap.read()

    #image reading
    imgS = cv.resize(src=img,dsize= (0, 0),fx= 0.25,fy= 0.25)
    imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    #setting up background
    background[162:162+480,55:55+640] = img
    background[44:44+633,808:808+414] = modeList[0]

    for encodeFace, FaceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)
        print("Match Index", matchIndex)

        if matches[matchIndex]:
            print("Known Face Detected")
            print(studentIds[matchIndex])


    cv.imshow("face_recognition",background)
    if cv.waitKey(1) == ord('q'):
        break
    