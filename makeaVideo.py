# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:20:12 2018

@author: Dell
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/Users\Dell\Documents\GitHub\capstoneproject\ProjectS\sample\example_03.mp4',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
   

        # write the flipped frame
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()