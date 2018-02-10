import cv2
import numpy as np

square = np.zeros((300,300), np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-2)
cv2.imshow('Square',square)
cv2.waitKey()

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow('Ellipse',ellipse)
cv2.waitKey()

cv2.destroyAllWindows()

#BITWISE OPERATIONS ON THESE IMAGES

#shows only where they intersect
And = cv2.bitwise_and(square,ellipse)
cv2.imshow('AND',And)
cv2.waitKey()

#shows where either square or ellipse is
bitwiseOr = cv2.bitwise_or(square,ellipse)
cv2.imshow('OR',bitwiseOr)
cv2.waitKey()

#shows where either exist by itself
bitwiseXor = cv2.bitwise_xor(square,ellipse)
cv2.imshow('XOR',bitwiseXor)
cv2.waitKey()

#shows everything that's not the part of square
bitwiseNot_sq = cv2.bitwise_not(square)
cv2.imshow('NOT -square',bitwiseNot_sq)
cv2.waitKey()

#last operation inverts the image totally
cv2.destroyAllWindows()