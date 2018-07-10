# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:49:18 2018

@author: Dell
"""

import tkinter as Tkinter

from tkinter import messagebox

import cv2
top = Tkinter.Tk()

filename = cv2.imread('messi.jpg')


image = Tkinter.Canvas.create_image(50, 50,image='C:/Users\Dell\Documents\GitHub\capstoneproject\ProjectS\messi.jpg')

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()