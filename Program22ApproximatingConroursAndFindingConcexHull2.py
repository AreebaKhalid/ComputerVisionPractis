import numpy as np
import cv2

image = cv2.imread('images/hand.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image',image)
cv2.waitKey(0)

#Threshold the image
ret, thresh = cv2.threshold(gray,176,255,0)

#find contours
ret, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#convex hull is smallest convex polygon that contains all points of it
# OR smallest polugon that can fix around the object itself

#sort contors by area and ten remove the largest frame contour
#This will happem only in white backround
n = len(contours) -1
#sort everything except largest contour
contours = sorted(contours,key=cv2.contourArea,reverse=False)[:n]

#Iterate throgh contours and draw the convex hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(0,255,0),2)
    cv2.imshow('Convex hull', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
