import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

#Creating a matrix of ones and multiply it by a scalar of 75
#This gives a matrix of all values 75 with same dimesnions as we have specified image.shape (image and thi matrix will add only when both have same dimensions)
M = np.ones(image.shape, dtype='uint8') * 75
#multiplying hy 175 so that when we add the values will exceel 255 so it will be more white and when we subtract there will 0s which makes image blacker

#adding matrix M with image ->increasing Brightness
added = cv2.add(image,M)
cv2.imshow('Added - increase Brightness',added)

#subtracting --> decrease Brightnesss
subtracted = cv2.subtract(image,M)
cv2.imshow('Subtracted - Decreasing Brightness',subtracted)

cv2.waitKey()
cv2.destroyAllWindows()
