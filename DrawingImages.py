#Author - Deepak 
#Date - 25/May/2019
#Descr - This example explains how to draw images and shapes using OpenCV.

import cv2
import numpy as np

#Images are stored in computer as multi dimensional array
#Creating an image using numpy array
image = np.zeros((700,700,3), np.uint8)

image_bw = np.zeros((700,700), np.uint8)

#Display the created canvas image
cv2.imshow("Sample Image ", image)
cv2.imshow("Sample Image - Black and white ", image_bw)

#OpenCV coordinates starts with top left corner.

#Drawing Blue Line
cv2.line(image, (0,0), (100,100), (255,127,0), 5)
cv2.imshow("Blue Line", image)

#Drawing Rectangle
cv2.rectangle(image, (200, 0), (400, 200), (0,255,0), 4)
cv2.imshow("Rectangle", image)

#Drawing Circle
cv2.circle(image, (250,350), 70, (0,0,255), -1)
cv2.imshow("Circle ", image)

#Adding Text to Image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV ',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Text ", image)

if cv2.waitKey(0) & 0xFF == ord('q'):
   cv2.destroyAllWindows()