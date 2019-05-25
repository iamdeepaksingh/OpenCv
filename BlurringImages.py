#Author - Deepak 
#Date - 26/May/2019
#Descr - Convolution and Blurring in OpenCv.

#Blurring of an image is a mathematical function where we average the pixels within a kernel region.

import cv2
import numpy as np

image = cv2.imread('images/image004.jpg')
cv2.imshow('Original Image', image)

# 3 x 3 kernel
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# v2.fitler2D to convolute the kernal with an image 
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)


# 7 x 7 kernel
kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred2)

# Averaging done by convolving the image with a normalized box filter. 
# This takes the pixels under the box and replaces the central element
# Box size needs to odd and positive 
blur = cv2.blur(image, (3,3))
cv2.imshow('Averaging BoX Filter', blur)

# Gaussian kernel, emphasis is on the points around center smoothens and reduces noise.
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)


# Takes median of all the pixels under kernel area and central 
# element is replaced with this median value
# We get paint kinf of effect.
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)


# Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)



if cv2.waitKey(0) & 0xFF == ord('q'):
   cv2.destroyAllWindows()