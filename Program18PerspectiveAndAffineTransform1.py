import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/scan.jpg')

cv2.imshow('Original',image)
cv2.waitKey()

#Coordinates of the 4 ccorner of the original image
points_A = np.float32([[320,15],[700,215],[85,610],[530,780]])

#Co-ordinates of the 4 corners of the desired output
# we use a ratio of an A4 paper 1:.41
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

#use thhe two sets of foir points to compute
# the perspective Transformation matrix, M
M = cv2.getPerspectiveTransform(points_A,points_B)

warped = cv2.warpPerspective(image,M,(420,594))

cv2.imshow('warpPerspective',warped)
cv2.waitKey()
cv2.destroyAllWindows()
