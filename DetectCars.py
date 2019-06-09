#Author: Deepak
#Date: 02/Jun/2019
#Descr: Car Detection using OpenCV haar cascade classifier.


'''
This code use haar cascade classifiers from OpenCV library.
Classifiers are downloaded from https://github.com/andrewssobral/vehicle_detection_haarcascades/blob/master/cars.xml
'''


import cv2
import numpy as np 
import time

'''
This function receives an image and detects car using car classifier.
'''

def detect_cars(source):

	car_classifier_obj = cv2.CascadeClassifier('CascadeClassifier/haarcascade_car.xml')
	gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
	cars = car_classifier_obj.detectMultiScale(gray, 1.4, 2)

	for (a,b,c,d) in cars:
		cv2.rectangle(source, (a,b), (a+c, b+d), (0,0,255), 2)
	return source



cap = cv2.VideoCapture('images/cars.avi')

while cap.isOpened():

	time.sleep(0.05)
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

	cv2.imshow('Detect Cars', detect_cars(frame))

	if cv2.waitKey(1) == 13:
		break;

if cv2.waitkey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

