# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:11:16 2022

@author: atakan
"""


import cv2
import numpy as np
from math import atan2, cos, sin, sqrt, pi
import csv
from time import time
value_d=[]
previous = time()
file = open('test.csv', 'w')

def drawAxis(img, p_, q_, colour, scale):
    p = list(p_)
    q = list(q_)
    
    angle = atan2(p[1] - q[1], p[0] - q[0]) # angle in radians
    hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * cos(angle)
    q[1] = p[1] - scale * hypotenuse * sin(angle)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
    # create the arrow hooks
    p[0] = q[0] + 9 * cos(angle + pi / 4)
    p[1] = q[1] + 9 * sin(angle + pi / 4)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
    p[0] = q[0] + 9 * cos(angle - pi / 4)
    p[1] = q[1] + 9 * sin(angle - pi / 4)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
def getOrientation(pts, img):
    current_time = time()- previous
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
        data_pts[i,0] = pts[i,0,0]
        data_pts[i,1] = pts[i,0,1]
    # Perform PCA analysis
    mean = np.empty((0))
    
    mean, eigenvectors, eigenvalues = cv2.PCACompute2(data_pts, mean)
    # Store the center of the object
    cntr = (int(mean[0,0]), int(mean[0,1]))
    
    
    cv2.circle(img, cntr, 3, (255, 0, 255), 1)
    p1 = (cntr[0] + 0.035 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.035 * eigenvectors[0,1] * eigenvalues[0,0])
    p2 = (cntr[0] - 0.035 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.035 * eigenvectors[1,1] * eigenvalues[1,0])
    drawAxis(img, cntr, p1, (0, 255, 0), 1)
    drawAxis(img, cntr, p2, (255, 255, 0), 1)
    angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
    value_elp=[round(np.sqrt((cntr[0]-p1[0])**2+(cntr[1]-p1[1])**2),3),round(np.sqrt((cntr[0]-p2[0])**2+(cntr[1]-p2[1])**2),3)]
    cv2.putText(img, str(value_elp), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    if ((round(current_time)%5) ==0):
        value=[value_elp[0],value_elp[1],angle,current_time]
        value_d.append(value)
    return angle,value_d

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('fdr.webm')

while cap.isOpened():
    res, img = cap.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_b = np.array([20, 0, 0])
    u_b = np.array([255, 255, 100])
    mask = cv2.inRange(hsv, l_b, u_b)
    #mask = cv2.erode(mask, None, iterations=3)
    mask = cv2.erode(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations=2)
    mask = cv2.dilate(mask, None, iterations=3)
    #ret, thresh = cv2.threshold(imgray, 0, 50, 0)

    #mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contours]
    # Calculate the area of each contour
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    area = cv2.contourArea(cnt)
    #area = cv2.contourArea(c)
    # Ignore contours that are too small or too large
    if area > 5e4 and 6e4 > area:
        continue
    angle,value_data=getOrientation(cnt, img)

        # Draw each contour only for visualisation purposes
    cv2.drawContours(img, contours, 0,(0, 255, 0), 1)
    cv2.imshow('Image', img)
    if res==False:
        writer = csv.writer(file)
        writer.writerows(value_data)
        break
    if cv2.waitKey(1) & 0xFF == 27:
        writer = csv.writer(file)
        writer.writerows(value_data)
        break
cap.release()
cv2.destroyAllWindows()
file.close()