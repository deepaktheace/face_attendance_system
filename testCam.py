import cv2 

    
def return_camera_index():
        Index = -2
        arr = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(Index)
            if cap.read()[0]:
                arr.append(Index)
                cap.release()
            Index += 1
            i -= 1
            print(arr)
while True:
    return_camera_index()
    print(return_camera_index(),'\n')

    if return_camera_index() != None:
        print(return_camera_index())
        break