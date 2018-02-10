import cv2
import numpy as np

image = cv2.imread('./images/elephant.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey()

#creating a 3x3 kernel
#dividing by 9 so that sum is 1
kernel_3x3 = np.ones((3,3),np.float32) / 9

#we use the cv2.filter2D to convolve the kernel with image
blurred = cv2.filter2D(image,-1,kernel_3x3)
cv2.imshow('3x3 Kernel Blurring',blurred)
cv2.waitKey()

#creating 7x7 kernel
kernel_7x7 = np.ones((7,7),np.float32) / 49

blurred2 = cv2.filter2D(image,-1,kernel_7x7)
cv2.imshow('7x7 Kernel Blurring',blurred2)
cv2.waitKey()

cv2.destroyAllWindows()