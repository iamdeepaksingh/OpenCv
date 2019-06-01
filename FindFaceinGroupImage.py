#Author: Deepak
#Date: 01/Jun/2019
#Descr: Finding an object image in a larger image using template matching in OpenCV.

import cv2
import numpy as np 

image = cv2.imread('images/GroupPic.jpg')
cv2.imshow('Original Image', image)

#Convert to Gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/friend.jpg', 0)
Height, Width = template.shape[:2]

result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF)
min_val ,max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 130, top_left[1] + 130)
cv2.rectangle (image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow('Locating Image', image)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

