import cv2 as cv 
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials,storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://realtimefaceattendance-53e9b-default-rtdb.firebaseio.com/",
    'storageBucket':'realtimefaceattendance-53e9b.appspot.com',
})

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

imageFolderPath = 'Images'
imagePathList = os.listdir(imageFolderPath)
studentIds = []
imgList = []
for path in imagePathList:
    imgList.append(cv.imread(os.path.join(imageFolderPath,path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{imageFolderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIds)

def findEncodings(imgList):
    encodeList = []
    for img in imgList:
        img = maintain_aspect_ratio_resize(cv.cvtColor(img,cv.COLOR_BGR2RGB),216,216)
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