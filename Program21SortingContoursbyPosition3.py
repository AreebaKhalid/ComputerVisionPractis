import cv2
import numpy as np

#functions we'll use or sorting by position

def x_cord_contour(contours):
    #Returns the X cordnate for the contour centroid
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours) #it returns center point of contor
        return (int(M['m10']/M['m00']))

def label_contour_center(image, c):
    #places a red circle on the centers of contours
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    #Draw the contour number on the image
    cv2.circle(image,(cx,cy),10,(0,0,255),-1)
    return image


#load our image
image = cv2.imread('images/bunchofshapes.jpg')

#create a copy of our original image
original_image = image.copy()

#grayscale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find canny edges
edged = cv2.Canny(gray,50,200)
cv2.imshow('1-Canny edges',edged)
cv2.waitKey(0)

#find contours and print how many were found
ret, contours, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('Numbers of contours found = ',len(contours))

#computer center of mass or centroids and draw them on our imae
for (i,c) in enumerate(contours):
    orig = label_contour_center(image,c)

cv2.imshow('Contours center',image)
cv2.waitKey(0)

#sort be left to right using our x_cord_contour function (small to large means smaller x cordinates
#  (on the left of image) to larger x cordinates(on roght of image)
contours_left_to_right = sorted(contours,key=x_cord_contour,reverse=False)

#labelling contours from left to right
for (i,c) in enumerate(contours_left_to_right):
    cv2.drawContours(original_image,[c],-1,(0,0,255),3)
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(original_image,str(i+1),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    cv2.imshow('Left to right contour',original_image)
    cv2.waitKey()
    (x, y, w, h) = cv2.boundingRect(c)

    #let's now crop each contour and save these image
    cropped_contour = original_image[y:y+h,x:x+w]
    image_name = "output_shape_number_"+str(i+1)+".jpg"
    print(image_name)
    cv2.imwrite(image_name,cropped_contour)

cv2.destroyAllWindows()

#enumerate to count i