'''
Created on 12 May 2019

@author: shai
'''

import os
import numpy as np
import cv2
from django.conf.locale import el
from cv2 import imwrite
import sys

def isBlack():
    a= []
    dif = cv2.imread("tempDif.jpg")
    
    for outter in dif:
        for pix in outter:
            total = int(pix[0])+int(pix[1])+int(pix[2])
            if total<150:    
                pix[0]=pix[1]=pix[2]=0
            new_total = int(pix[0])+int(pix[1])+int(pix[2])
    
            a.append(new_total)
        tempMax = 0;
    for el in a:
        if el>tempMax:
            tempMax = el
        else:
            continue
    if(tempMax>0):
        return False
    else: return True


def isEqual(cur,prev):

    difference = cv2.subtract(cur,prev)
    cv2.imwrite("tempDif.jpg",difference)
    dif = cv2.imread("tempDif.jpg",0)

    if(isBlack()):
        os.remove("tempDif.jpg")
        return True
    else: 
        os.remove("tempDif.jpg")
        return False
    
filename = sys.argv[1]
cap = cv2.VideoCapture(filename)

try:
    if not os.path.exists(filename[0:4]):
        os.makedirs(filename[0:4])
except OSError:
    print("Error")
    
currentFrame = 0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
noUnique = 0
while(currentFrame<length):
    cap.set(1, currentFrame)
    ret, frame = cap.read()    
    if currentFrame ==0:
        firstName = filename[0:4]+'/slide'+str(currentFrame)+'.jpg'
        cv2.imwrite(firstName,frame)
    else:   
        nameCur = filename[0:4]+'/slide'+str(currentFrame)+'.jpg'
        cv2.imwrite(nameCur,frame)
        cur = cv2.imread(nameCur)
           
        namePrev = filename[0:4]+'/slide'+str(currentFrame-500)+'.jpg'
        prev = cv2.imread(namePrev)
        noSeconds = (currentFrame/25)
        noMinutes = round((noSeconds/60),2)
        if isEqual(cur,prev):
            os.remove(namePrev)

        else: 
            print("Frame number ", currentFrame, "is a new frame that appears about ",noMinutes, " minutes in" )
            noUnique +=1
              
    currentFrame +=500

print("There were ", noUnique, "unique frames identified.")