import cv2
import numpy as np

#load image as gray scale
image = cv2.imread('./images/gradient.jpg',0)
#threshlding only applies to gray scaele
#it converst grayscale image to binary

#Values below 127 goes to 0(black, everything abpve goes to 255 (white))
#cv2.threshold((image,threshold,maxValue,typeofThreshold))
ret, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary',thresh1)

#Values below 127 goes to 255 and values above 127 go to 0(reverse of avove)
ret, thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse',thresh2)

#Values above 127 are truncated (held) at 127 (the 255 argument is unused)
ret, thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC',thresh3)

#Values below 127 g to 0 above 127 are unchanged
ret, thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO',thresh4)

#Reverse of above, below 127 is unchanged above 127 goes to 0
ret, thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV',thresh5)

cv2.waitKey()
cv2.destroyAllWindows()
