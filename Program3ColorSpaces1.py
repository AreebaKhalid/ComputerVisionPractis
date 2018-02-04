import cv2

image = cv2.imread('./images/input.jpg')
#BGR value for the very first pixel
B, G, R = image[0,0]
print(B, G, R)
print(image.shape)

#image shape is now only two dimwnsions  because converting into grayscale actually we arre converting into 2 dimension array
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
#it will print only 1 value here
print(gray_img[0,0])