import cv2
#import numpy as np

def get_contour_areas(contors):
    #returns the areas of all contours on list
    all_areas = []
    for cnt in contors:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#load our image
image = cv2.imread('images/bunchofshapes.jpg')

#create a copy of our original image
original_image = image

#grayscale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find canny edges
edged = cv2.Canny(gray,50,200)
cv2.imshow('1-Canny edges',edged)
cv2.waitKey(0)

#find contours and print how many were found
ret, contours, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('Numbers of contours found = ',len(contours))

#printing contours before sorting
print("Contor Areas before sorting")
print(get_contour_areas(contours))

#sort contours large to small (reverse = false will sort small to large)
sorted_contours = sorted(contours,key=cv2.contourArea,reverse=True)

print("Contor Areas after sorting")
print(get_contour_areas(sorted_contours))

#Iterate over our contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(original_image,[c],-1,(255,0,0),3)
    cv2.waitKey()
    cv2.imshow('Contours By Area',original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.destroyAllWindows()
