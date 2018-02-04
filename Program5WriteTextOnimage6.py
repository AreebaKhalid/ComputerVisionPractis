import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)

#cv2.putText(image,text,bottomleft startpoint,font , font size, color, thickness)
cv2.putText(image, 'Hello World!',(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
cv2.imshow("Hellow World",image)
cv2.waitKey()
cv2.destroyAllWindows()