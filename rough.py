import cv2

img = cv2.imread('Resources/background.png')
img2 = cv2.imread('Images/100234.png')
print(img.shape,'\n',img2.shape)