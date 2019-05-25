#Author - Deepak 
#Date - 25/May/2019
#Descr - Erosion and Dilation in OpenCv.

#Erosion and Dilation are morphological functions provided by OpenCv.

import cv2
import numpy as np

image = cv2.imread('images/alphabet.jpg', 0)

cv2.imshow('Original', image)


# Let's define our kernel size
kernel = np.ones((15,15), np.uint8)

# Erosion is removing pixels at boundaries of an object in an image.
#Erosion makes the object in white smaller.
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)


#Dilation is adding pixels at the boundaries of an object in an image.
#Dilation makes the object in white bigger.
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)


# Opening - Good for removing noise
#Opening is Erosion followed by Dilation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)


# Closing - Good for removing noise
#Closing is Dilation followed by Erosion.
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)


if cv2.waitKey(0) & 0xFF == ord('q'):
   cv2.destroyAllWindows()