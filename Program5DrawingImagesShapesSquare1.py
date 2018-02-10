import cv2
import numpy as np
#np.zeros((height,width,RGB))
#black image
image = np.zeros((512,512,3),np.uint8)

#black and white grayscale imae
image_bw = np.zeros((512,512),np.uint8)

cv2.imshow('Black Rectangle(Color)', image)
cv2.imshow('Black Rectangle (B&W)',image_bw)

cv2.waitKey()
cv2.destroyAllWindows()
