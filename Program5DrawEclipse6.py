import cv2
import numpy as np

ellipse = np.zeros((300,300),np.uint8)
#image,center,axes,angle,start angle,end angle ,color,thickness
cv2.ellipse(ellipse,(150,150),(150,150),30, 0,180,255,-1)
cv2.imshow('Ecllipse',ellipse)
cv2.waitKey()
cv2.destroyAllWindows()