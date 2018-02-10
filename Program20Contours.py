import cv2
import numpy as np

#loading image
image = cv2.imread('images/shapes_donut.jpg')
image2 = cv2.imread('images/shapes_donut.jpg')

cv2.imshow('Input Image',image)
cv2.waitKey(0)

#grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#find canny edges
edged = cv2.Canny(gray, 30,200)
edged2 = cv2.Canny(gray, 30,200)

cv2.imshow('Canny Edges',edged)
cv2.waitKey(0)

#Finding contours
#FinfContours method alter the image so if u dont want to change the image use a copy of image eg edged.copy()
ret, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
ret2, contours2, hierarchy2 = cv2.findContours(edged2, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#ret is boolean indicator if the function was successfully run
#countours are stored as numpy array of(x,y) points that form the countour
#hierarchy describe the child-parent relationships between the contours(i.e contours within contours)

#findContours(image,retrieval mode, approximation method)
#CHAIN_APPROX_NONE stores all boundary points
#CHAIN_APPROX_SIMPLE onlu provides start and end points of bounding contours
#RETR_EXTERNAL retrieves external or outer contours only
#RETR_LIST retrieves all contours
cv2.imshow('Canny edges after contouring',edged2)
cv2.waitKey(0)

#Countours is list of list
print(contours)
print('Numbers of contours found = '+str(len(contours)))

#Draw all counters
#use -1 as the 3rd arameter to draw all
cv2.drawContours(image, contours,-1,(0,255,0),3)
cv2.drawContours(image2, contours2,-1,(0,255,0),3)

cv2.imshow('Countours EXTERNAL',image)
cv2.waitKey(0)
cv2.imshow('Countours LIST',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
