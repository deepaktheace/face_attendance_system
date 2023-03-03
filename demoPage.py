import customtkinter
import os
from PIL import Image
from tkinter import CENTER
import os 
import cv2 as cv 
import numpy as np
import pickle
from cvzone import cornerRect
import firebase_admin
from firebase_admin import credentials,db,storage
from time import sleep
from datetime import datetime

print("hello")
img = cv.imread("Resources/Modes/2.png")
cv.imshow("img",img)
cv.waitKey(0)