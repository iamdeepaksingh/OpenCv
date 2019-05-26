#Author - Deepak 
#Date - 26/May/2019
#Descr - Hough Transform for lane detection

# Hough Transform is used to detect straight lines.
# They can be used in lane detection in self driving cars, the quality depends on the quality of edges calculation.


import cv2
import numpy as np 

image = cv2.imread('images/sudoku.png')

#Gray Scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract Edges
edges = cv2.Canny(gray_image, 50, 200)


'''
HoughLinesP - Arguements (taken from OpenCV documentation)
cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

dst: Output of the edge detector. It should be a grayscale image (although in fact it is a binary one)
lines: A vector that will store the parameters (r,θ) of the detected lines
rho : The resolution of the parameter r in pixels. We use 1 pixel.
theta: The resolution of the parameter θ in radians. We use 1 degree (CV_PI/180)
threshold: The minimum number of intersections to "*detect*" a line
srn and stn: Default parameters to zero. Check OpenCV reference for more info.

'''

# Using Hough Transform Porbabilistic
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 250, minLineLength=10, maxLineGap=250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

cv2.imshow('Hough lines', image)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()



