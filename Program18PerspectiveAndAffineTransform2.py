import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/ex2.jpg')
rows, cols, ch = image.shape

cv2.imshow('Original Imahe',image)
cv2.waitKey()

#Cordinates of the image
# hete we need only 3 coordinates to otain correct transform
#it maintain parallelism (basically its rotating image)
points_a = np.float32([[320,15],[700,215],[85,610]])

#cordinate of desired output
# we use a raionof an A4 paper 1: 1.41
points_b = np.float32([[0,0],[420,0],[0,594]])

#use two sets of points to compute
#the affine transorm M
M = cv2.getAffineTransform(points_a,points_b)

warped = cv2.warpAffine(image,M,(cols,rows))
cv2.imshow('warpPerspective',warped)
cv2.waitKey()

cv2.destroyAllWindows()