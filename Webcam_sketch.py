#Author - Deepak 
#Date - 26/May/2019
#Descr - Sketch using Webcam in OpenCV.

'''
We use VideoCapture to capture the frames from webcam,
Loop through each frame
Convert to Gray scale
Use Gaussian Blur
Detect the edges using Canny
Apply Binary Threshold Inverse
'''
import cv2
import numpy as np

# This generates sketch of the frames captured by Webcam
def sketch(image):

    if (type(image) is np.ndarray):
        # Convert image to grayscale
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Clean up image using Guassian Blur
        img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
        # Extract edges
        canny_edges = cv2.Canny(img_gray_blur, 15, 70)
    
        # Do an invert binarize the image 
        ret, mask = cv2.threshold(canny_edges, 80, 255, cv2.THRESH_BINARY_INV)
        return mask
    else:
        pass    


# VideoCapture to read frames from Webcam
cap = cv2.VideoCapture(0)
#i = 0
while True:
    ret, frame = cap.read()
    cv2.imshow('*** Webcam Sketch ***', sketch(frame))
    #cv2.imwrite('opencv'+str(i)+'.png', frame)
    #i = i+1
    if cv2.waitKey(0) == 13:
        break
    elif cv2.waitKey(0) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
            
        
# Release camera and close windows if 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cap.release()
    cv2.destroyAllWindows()