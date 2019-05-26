#Author - Deepak 
#Date - 26/May/2019
#Descr - Hough Transform for circle detection.

import cv2
import numpy as np 

image =  cv2.imread('images/coins.jpg')
cv2.imshow("original image", image)

#Gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Median Blue to reduce noise
image_blur = cv2.medianBlur(gray_image, 5)

#Hough Transform
circles = cv2.HoughCircles(image_blur, cv2.HOUGH_GRADIENT, 1, image.shape[0]/64, param1 = 200, param2 = 10, minRadius = 5, maxRadius = 30)

#Draw the detected circles
if circles is not None:
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		#Draw outer circle
		cv2.circle(image, (i[0], i[1]), i[2], (0,255,0), 2)
		#Draw the inner circle
		cv2.circle(image, (i[0], i[1]), 2, (0,0,255), 3)

cv2.imshow('Circles Detected', image)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

