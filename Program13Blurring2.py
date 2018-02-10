import cv2
import numpy as np

image = cv2.imread('./images/elephant.jpg')

#Averaging done by convolving the image with a normalized box filter.
#This takes the pixels under the box and replaces the central element
#Box size needs to odd and positive

blur = cv2.blur(image,(3,3))
cv2.imshow('Averaging',blur)
cv2.waitKey()

#instead of box filter, guassian kernel
Guassian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Guassina Blurring', Guassian)
cv2.waitKey()

#Takes median of all the pixels under kernel area and central
#element is reolaced with the median value
median = cv2.medianBlur(image,5)
cv2.imshow('MedianBlurring',median)
cv2.waitKey()
#Bilateral is very effective in noise removal while keeping edges sharp
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral Blurring',bilateral)
cv2.waitKey()

cv2.destroyAllWindows()