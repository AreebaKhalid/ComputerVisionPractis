import numpy as np
import cv2

image = cv2.imread('./images/elephant.jpg')

cv2.imshow('Original',image)
cv2.waitKey()

#Parameters, after None are -the filter strength 'h' (5-10 is a good range)
#Next is hforColorComponents, set as same value as h again

dst = cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)

cv2.imshow('Fast means denoising', dst)
cv2.waitKey()

cv2.destroyAllWindows()