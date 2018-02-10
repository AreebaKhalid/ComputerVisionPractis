import cv2
import numpy as np

#load our image
image = cv2.imread('images/bunchofshapes.jpg')
cv2.imshow('0-Original Image', image)
cv2.waitKey(0)

#create a black image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1],3))

#create a copy of our original image
original_image = image

#grayscale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find canny edges
edged = cv2.Canny(gray,50,200)
cv2.imshow('1-Canny edges',edged)
cv2.waitKey(0)

#find contours and print how many were found
ret, contours, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('Numbers of contours found = ',len(contours))

#Draw all contours
cv2.drawContours(blank_image, contours,-1,(0,255,0),3)
cv2.imshow('2-all contours over blank image', blank_image)
cv2.waitKey(0)

#draw all contours over original image
cv2.drawContours(image, contours,-1,(0,255,0),3)
cv2.imshow('3-all cntours ',image)
cv2.waitKey(0)

cv2.destroyAllWindows()
