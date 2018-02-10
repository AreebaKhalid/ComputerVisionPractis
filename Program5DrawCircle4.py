import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)

#cv2.circle(image,center,radius,color,fill)
cv2.circle(image,(350,350),100,(15,27,50),-1)

cv2.imshow("Circle",image)
cv2.waitKey()
cv2.destroyAllWindows()