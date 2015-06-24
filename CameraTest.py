# CameraTest.py

# -*- coding: utf-8 -*-

__author__ = "Saad Bin Shahid"


import cv2

cv2.namedWindow("Live Cam")
vc = cv2.VideoCapture(0)

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Live Cam", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Live Cam")