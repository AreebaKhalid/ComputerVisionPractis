import numpy as np
import cv2

#loading and gray scaling the image
image= cv2.imread('images/someshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Identifying the shapes',image)
cv2.waitKey(0)

ret, thresh = cv2.threshold(gray, 127,255,1)

#Extract contours
ret, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

for cnt in contours:

    #get approximate polygons
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

    if len(approx) == 3:
        shape_name = "Triangle"
        cv2.drawContours(image,[cnt],0,(0,255,0),-1)

        #find contour center to place text at the center
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(image, shape_name, (cx - 50,cy), cv2.FONT_HERSHEY_SIMPLEX,1 ,(0,0,0), 1)

    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(cnt)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        #check to see if a 4-sided polygon is square or rectangle
        #cv2.boundRect returns the top left and witdh
        if abs(w-h) <= 3: #because w and h are pixels form point x and y
            shape_name = "Square"

            #Find contour center to place text at the center
            cv2.drawContours(image,[cnt],0,(0,125,255),-1)
            cv2.putText(image,shape_name,(cx - 50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        else:
            shape_name = "Rectangle"

            #find contour center to place text at the center
            cv2.drawContours(image, [cnt], 0, (0, 0, 255), -1)
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 10:
        shape_name ="star"
        cv2.drawContours(image,[cnt],0,(255,255,0),-1)

        # find contour center to place text at the center
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) >= 15:
        shape_name ="circle"
        cv2.drawContours(image,[cnt],0,(0,255,255),-1)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(image, shape_name, (cx - 50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    cv2.imshow('Identifying shapes',image)
    cv2.waitKey(0)

cv2.destroyAllWindows()