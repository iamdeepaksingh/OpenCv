#Author - Deepak 
#Date - 28/May/2019
#Descr - Finding Blueman using template matching in OpenCV.

import numpy as np 
import cv2

image = cv2.imread('images/fruits.jpg')
#cv2.imshow("Where is Blueman ?", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/strawberry.jpg', 0)
Height, Width = template.shape[:2]

result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF)
min_val ,max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + Width, top_left[1] + Width)
cv2.rectangle (image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow('Where is Blueman ?', image)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

