# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:57:40 2018

@author: Dell
"""
import numpy as np
import cv2

cap = cv2.VideoCapture('D:\projectS\basic-motion-detection\videos\example_01.mp4')
    
cap.isOpened()

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame',frame)   
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()