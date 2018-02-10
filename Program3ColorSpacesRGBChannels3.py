import cv2

image = cv2.imread('./images/input.jpg')

#split function will split the image into each color index
R, G, B = cv2.split(image)

print(B.shape)
cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)
cv2.waitKey()
cv2.destroyAllWindows()

#merge = to remake original image
merged = cv2.merge([B, G, R])
cv2.imshow('Merged',merged)

#amplify the blue color
merged = cv2.merge([B+100,G,R])
cv2.imshow('Merged with Blue amplified',merged)

cv2.waitKey()
cv2.destroyAllWindows()