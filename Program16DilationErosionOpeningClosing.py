#Dilation - add pixels to boundary -thining effect.....
#erosion - remove pixels ad boundary -- thickening effect....
#black text on white background...
#Dilation will  make text thin as its boubdary pixels are white which are added
#Erosion- inverse

#Opening is erosion followd by dilation
#Closing is dilation followd by erosion
#use =  to remove noise

import cv2
import numpy as np

image = cv2.imread('./images/opencv_inv.png')


cv2.imshow('Original', image)
cv2.waitKey()

#fdefining kernel size
kernel = np.ones((5,5),np.uint8)

#Erode
erosion = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erosion',erosion)
cv2.waitKey()

dilation = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilation',dilation)
cv2.waitKey()

#iterations 2 or more to increase the effect

#Opening
opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('Opeening',opening)
cv2.waitKey()

#Closing
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('Closing',closing)
cv2.waitKey()

cv2.destroyAllWindows()