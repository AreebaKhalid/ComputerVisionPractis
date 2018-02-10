#better way of thresholding
import cv2
import numpy as np

#Load our image
image = cv2.imread('./images/Origin_of_Species.jpg',0)

cv2.imshow('Original',image)
cv2.waitKey(0)

#Values below 127 goes to 0(black) everything above goes to 255(white)
ret, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary',thresh1)
cv2.waitKey()

#It's good practise to blur images as it removes noise
image = cv2.GaussianBlur(image,(3,3),0)

#Using Adaptive Threshold
#src,maxValue,adaptiveMethod,thresholdtype,blocktype,constant that is subtracted form mean
#block size must be odd number
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow('Adaptive Mean thresholding',thresh)
cv2.waitKey()

_,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu \'s Thresholding',th2)
cv2.waitKey()

#Otsu's thresholding after Guassian filtering
blur = cv2.GaussianBlur(image,(5,5),0)
_,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Guassian Otsu\'s Thresholding',th3)
cv2.waitKey()
cv2.destroyAllWindows()