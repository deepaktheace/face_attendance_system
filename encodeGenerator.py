import cv2 as cv 
import face_recognition
import pickle
import os

imageFolderPath = 'Images'
imagePathList = os.listdir(imageFolderPath)
studentIds = []
imgList = []
for path in imagePathList:
    imgList.append(cv.imread(os.path.join(imageFolderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)

def findEncodings(imgList):
    encodeList = []
    for img in imgList:
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
#print(encodeListKnown[0])
print("Encoding Complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("file saved")