# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:17:19 2018

@author: Dell
"""

import numpy as np
import cv2
import time

starttime = time.time()

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
 # return a single frame in variable `frame`

i=0;

# Define the codec and create VideoWriter object

while(cap.isOpened()):
    ret, frame = cap.read() 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imwrite('C:/Users/Dell/Documents/GitHub/capstoneproject/images/photo'+str(i)+'.png',frame)
    var = time.time() - starttime  
    #print(var)
    if ((var) > 20):
        break
    i = i+1
    
    #you can change the sleeping time if you want.
    time.sleep(0.005)
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()