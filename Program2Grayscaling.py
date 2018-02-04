import cv2

# image = cv2.imread('./images/input.jpg')
# cv2.imshow('Original', image)
# cv2.waitKey()
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Grayscale',gray_image)
# cv2.waitKey()

#Another Faster Method

img = cv2.imread('./images/input.jpg',0)
cv2.imshow('Grayscale',img)
cv2.waitKey()
cv2.destroyAllWindows()