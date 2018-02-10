import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')
cv2.imshow('Original Image', image)

#Creating our sharpening kernel, we don't normalize since the values in matrix sum to 1
kernel_sharpeing = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]])
#applying different kernels to input image
sharpened = cv2.filter2D(image,-1,kernel_sharpeing)

cv2.imshow('Image Sharpening',sharpened)

cv2.waitKey()
cv2.destroyAllWindows()