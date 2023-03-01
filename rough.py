import cv2
from time import sleep
img = cv2.imread('Resources/background.png')
img2 = cv2.imread('Images/krishna.jpg')
print(img2.shape)
sleep(5)
img2 = cv2.resize(img2,(460,259))
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original",img2)
cv2.imshow("BlueScale",img2_rgb)
cv2.imshow("GrayScale",img2_gray)
cv2.waitKey(0)