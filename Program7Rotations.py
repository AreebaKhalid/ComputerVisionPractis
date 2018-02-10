import cv2
import  numpy as np

image = cv2.imread('./images/input.jpg')
height, width = image.shape[:2]

#cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y,angle_of_rotation,scale)
#angle is anti clockwise
#image is cropped by putting scale = 1
#put = .5 it will not crop
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,.5)
#new width and height in warp_affine function
rotated_image = cv2.warpAffine(image, rotation_matrix,(width,height))

cv2.imshow("Rotated Image",rotated_image)

#method-2
image = cv2.imread('./images/input.jpg')
rotated_image = cv2.transpose(image)
cv2.imshow("Rotated Image - Method 2",rotated_image)

cv2.waitKey()
cv2.destroyAllWindows()
