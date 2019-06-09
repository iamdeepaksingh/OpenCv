#Author: Deepak
#Date: 09/Jun/2019
#Descr: Pedestrian Detection using OpenCV full body haar cascade classifier.


'''
This code use haar cascade classifiers from OpenCV library.
Classifiers are downloaded from https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

import cv2
import numpy as np 


'''
This function gets an image frame, detects a pedestrian using
full body haar cascade classifier and draws a rectangle around them.
'''
def pedestrian_detect(source):

	pedestrian_classifier = cv2.CascadeClassifier('CascadeClassifier/haarcascade_fullbody.xml')

	gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

	pedestrians = pedestrian_classifier.detectMultiScale(gray, 1.2, 3)

	for (a,b,c,d) in pedestrians:
		cv2.rectangle(source, (a,b), (a+c, b+d), (0,0,255), 2)
	return source


# Read from source	
cap = cv2.VideoCapture('images/walking.avi')

# process frame one by one
while cap.isOpened():
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

	cv2.imshow('Pedestrians', pedestrian_detect(frame))
# Press Enter to come out of loop
	if cv2.waitKey(1) == 13:
		break;

# press q to quit
if cv2.waitkey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


