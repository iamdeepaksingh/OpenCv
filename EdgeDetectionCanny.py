#Author - Deepak 
#Date - 26/May/2019
#Descr - Canny Edges Detection in OpenCv.

# There are three main types of edge detection
# Sobal, laplacian and Canny



import cv2
import numpy as np

image = cv2.imread('images/shape.jpg',0)

height, width = image.shape

# Extract Sobel Edges
# Sobel emphasises on vertical or horizontal edges.
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('Original', image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel Bitwise OR', sobel_OR)

#Laplacian emphasises on all orientations.
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)


##  Then, we need to provide two values: threshold1 and threshold2. Any gradient value larger than threshold2
# is considered to be an edge. Any value below threshold1 is considered not to be an edge. 
#Values in between threshold1 and threshold2 are either classiﬁed as edges or non-edges based on how their 
#intensities are “connected”. In this case, any gradient values below 60 are considered non-edges
#whereas any values above 120 are considered edges.

# Canny Edge Detection uses gradient values as thresholds
# The first threshold gradient

'''
# Canny Edge detection developed by John F. Canny in 1896

1. applies gaussian blurring
2. finds intensity gradient of the image
3. applies non max suppression (removes pixels which are not edges)
4. hysteresis - applies threshold (if the pixels is within the upper and lower threshold, it is considered an edge)   
'''

#Canny detects edges optimally because of low error rate and high accuracy.
canny = cv2.Canny(image, 60, 120)
cv2.imshow('Canny Edges', canny)

if cv2.waitKey(0) & 0xFF == ord('q'):
   cv2.destroyAllWindows()
