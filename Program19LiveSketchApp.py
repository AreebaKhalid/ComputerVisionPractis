import cv2
import numpy as np

#Sketch generating function:
def sketch(image):
    #Conbvert the image to grayscale
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Clean up image using Guassian blur ->to cleann up the noise
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    #extract edges
    canny_edges = cv2.Canny(img_gray_blur,10,70)

    #canny is black background with white edges

    #Do an inverse binarize the imahe
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

#Initialize the webcam, cap is the object provided by VideoCapture
#It contains a boolean indicatimg if it was successful (ret)
#It aslo contains the images collected from the webcam(frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our life sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the enter key
       break

#Release camera and close windows
cap.release()
cv2.destroyAllWindows()