import cv2

#loading image
input = cv2.imread('./images/input.jpg')
print(input.shape)

#print each dimesnion

print('Height of Image: ',int(input.shape[0]),' pixels')
print('Width of Image: ',int(input.shape[1]),' pixels')
#output (hight int pixels,pixels wide,3L means RGB to make image)
#display image
#first parameter = title shown on img window
#second parameter = image variable
cv2.imshow('Hello World',input)

#waitkey allows us to input info when a image window is open
#by leaving it blank it just waits for anykey to be pressed beforre
#continuing . By placing numbers we specify delay
#for how long to keep window open
cv2.waitKey()

#This close wall open windows
#if not placed program will hange
cv2.destroyAllWindows()

#imrite with filename and image to be saved to save it
cv2.imwrite('output.png',input)
cv2.imwrite('output.jpg',input)