#Author: Deepak
#Date: 02/Jun/2019
#Descr: Face and eye detection using Haar cascade classifier in OpenCV.

'''
This code use haar cascade classifiers from OpenCV library.
Classifiers are downloaded from https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

import cv2
import numpy as np


'''
This function receives an input image.
Converts it into grayscle to remove noise.
Then calls detectMultiScale with scale_factor 1.3
and min neighbours with 4 against a Haarcascade classifier.
'''
def face_detector(image):

	# Initialise an object of classifier
    face_classifier_obj = cv2.CascadeClassifier('CascadeClassifier/haarcascade_frontalface_default.xml')

    #Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_classifier_obj.detectMultiScale(gray_image, 1.3, 4)

    for (a,b,c,d) in faces:
	    result_face = cv2.rectangle(image, (a,b), (a+c, b+d), (0,0,255), 2)
    return result_face


'''
This function takes an image, detects eyes and
draws a rectangle aroud the detected eyes.
'''
def eye_detector(image):

    #Initialise eye haarcascade
    eye_classifier_obj = cv2.CascadeClassifier('CascadeClassifier/haarcascade_eye.xml')

    #grayscale
    #if(len(image.shape)) < 3:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    eyes = eye_classifier_obj.detectMultiScale(gray_image)

    for(a,b,c,d) in eyes:
    	result_eye = cv2.rectangle(gray_image, (a,b), (a+c,b+d), (0,0,255), 2)
    return cv2.cvtColor(result_eye, cv2.COLOR_GRAY2RGB)	


'''
This function takes an image, detects face and eyes and
draws a rectangle around it.
'''

def face_detector_webcam(image):

	# Initialise an object of classifier
    face_classifier_obj = cv2.CascadeClassifier('CascadeClassifier/haarcascade_frontalface_default.xml')
    eye_classifier_obj = cv2.CascadeClassifier('CascadeClassifier/haarcascade_eye.xml')

    #grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier_obj.detectMultiScale(gray, 1.3, 5)

    if faces is ():
    	return image

    

    for (a,b,c,d) in faces:
    	cv2.rectangle(image, (a,b), (a+c, b+d), (0,0,255), 2)
    	crop_gray = gray[b:b+d, a:a+c]
    	crop_color = image[b:b+d, a:a+c]

    	eyes = eye_classifier_obj.detectMultiScale(crop_gray)

    	for (p,q,r,t) in eyes:
    		cv2.rectangle(crop_color, (p,q), (p+r, q+t), (0,0,255), 2)

    	crop_color = cv2.flip(crop_color,1)
    	return crop_color	



#read the input image

input_image = cv2.imread('images/ElonMusk.jpg')
cv2.imshow('Original Image', input_image)
'''
cv2.imshow('Detected Face', face_detector(input_image))
cv2.imshow('Detected Eyes', eye_detector(input_image))
'''

#read from webcam
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('Face and Eye detection from webcam', face_detector_webcam(input_image))
	if cv2.waitKey(1) == 13:
		break;


if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

