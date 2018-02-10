import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')
height, width = image.shape[:2]

#start pixel coordinates (top left of cropped redctangle)
start_row, start_col = int(height * .25), int(width * .25)

#end pixel coordinates (bottom right)
end_row, end_col = int(height * .75), int(width * .75)

#using index to crop out the rectangleof desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow('Original Image', image)
cv2.waitKey()
cv2.imshow('Cropped Image', cropped)
cv2.waitKey()
cv2.destroyAllWindows()