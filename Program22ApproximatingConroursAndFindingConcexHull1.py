import numpy as np
import cv2

#load image and keep copy
image = cv2.imread('images/house.jpg')
orig_image = image.copy()
cv2.imshow('Original image',orig_image)
cv2.waitKey()

#grayscale and binarize
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

#find contours
ret, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#Iterate through eACH contour and compute the bounding rectanngle
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image,(x,y),(w+w,y+h),(0,0,255),2)
    cv2.imshow('Bounding Rectangle',orig_image)

cv2.waitKey()

#cv2.approxPolyDP(contour,ApproximationAccuracy,Closed)
#contour = is the individual contour we wish to approximate
#Approximation Acccuracy = important parameter is determing the accuracy of the approximation.
# Small values give precise-approximations, large values give more generic approximation .
# A good rule of thumb is les than 5% of the contour perimeter
#Closed = a boolean value that states whether the approximate contour should be open or closed



#Iterate through each contour and compute the approx xontour
for c in contours:
    #Calculate accuacy as a percent of the contour perimeter
    #less accuracy more accurate
    accuaracy = 0.03 * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,accuaracy,True)
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    cv2.imshow('Approx Poly DP',image)

cv2.waitKey()
cv2.destroyAllWindows()