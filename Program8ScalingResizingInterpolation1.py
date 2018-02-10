import cv2
import numpy as np

#loading image
image = cv2.imread('./images/input.jpg')

#let's make our image 3/4 of it's original size
#by default interpolation is linear

image_scaled = cv2.resize(image,None ,fx=0.75,fy=0.75)
#if u wnt to change in 1 dimension set fy=1  or fx to 1
cv2.imshow('Scaling - Linear Interpolation',image_scaled)
cv2.waitKey()

#doubling the size of image
image_scaled2 = cv2.resize(image,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cublic Interpolation',image_scaled2)
cv2.waitKey()

#resizing by setting exact dimensions
image_scaled2 = cv2.resize(image,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size',image_scaled2)
cv2.waitKey()

cv2.destroyAllWindows()