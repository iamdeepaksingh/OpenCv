#Author - Deepak 
#Date - 26/May/2019
#Descr - Finding Centroid

import cv2
import numpy as np 

image = cv2.imread("images/shape002.png")

# Gray Scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Binary Thresholding
ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

# Find contours
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Iterate through contours
for c in contours:
	M = cv2.moments(c)

	# Get the x, y co-ordinates of center
	cx = int(M['m10'] / M['m00'])
	cy = int(M['m01'] / M['m00'])

	cv2.circle(image, (cx, cy), 5, (255,255,255), -1)
	cv2.putText(image, "Centroid", (cx-25, cy-25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 0))

# Display the image
cv2.imshow("Final Image", image)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()