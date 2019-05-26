#Author - Deepak 
#Date - 26/May/2019
#Descr - Finding Contours using OpenCV

#Contours are continous lines or curves that bound the full boundary of an object in an image
#They are used in object detection and can process only gray scale image.

#OpenCV stores Contours in a list of lists.

import cv2
import numpy as np 

image = cv2.imread('images/shape.jpg')
cv2.imshow("Original Image", image)

# Gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect edges using Canny 
edges = cv2.Canny(gray_image, 30, 200)
cv2.imshow('Edges using Canny', edges)

#Finding contours
_, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Edges after contouring', edges)


'''
Approximation method CHAIN_APPROX_NONE stores all the boundary points,
whereas Simpy stores the endpoints

Retrieval mode gives hierarchy of contours
cv2.RETR_LIST - retrieves all contours
cv2.RETR_EXTERNAL - retrieves external or outer contours only
cv2.RETR_COMP -retrieves all in a 2 level hierarchy
cv2.RETR_TREE - retrieves all in full hierarchy
'''

print("Total number of contours is " +str(len(contours)))

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow("Contours ", image)

if cv2.waitKey(0) & 0xFF == ord('q'):
   cv2.destroyAllWindows()


