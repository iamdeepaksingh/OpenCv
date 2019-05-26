#Author - Deepak 
#Date - 26/May/2019
#Descr - Blob Detection.

import cv2
import numpy as np 

image = cv2.imread('images/sunflowers.jpg')
cv2.imshow('original image', image)

#Setup Blob Detector
detector = cv2.SimpleBlobDetector_create()

#Detect blobs
keypoints = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

'''
cv2.drawKeypoints(input image, keypoints, blank_output_array, color, flags)

flags:

cv2.DRAW_MATCHES_FLAGS_DEFAULT
cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
'''


#Display keypoints
cv2.imshow('Detected blobs', blobs)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()


