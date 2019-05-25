#Author - Deepak 
#Date - 23/May/2019
#Descr - This example explains how to convert an image into greyscale form using Open CV in Python.

import cv2

# Read the image. Open CV reads an image in multi dimentional array.
image = cv2.imread('image001.jpg')
cv2.imshow('Original', image)

# We use cvtColor, to convert to grayscale
# Grey scale images are in the shades of grey in the range 0-255, 
#Darker shades are represented by lower values.
# Grey Scale images are represented in 2 D array.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()




