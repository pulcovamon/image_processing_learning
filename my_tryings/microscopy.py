import cv2
import numpy as np


img_bgr = cv2.imread(r'topics_of_learning\geometric.jpg')

img_gray = img_bgr[:,:,0]

img = cv2.medianBlur(img_gray, 7)

ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

img = cv2.dilate(img, kernel = np.ones((5, 5), np.uint8))
img = cv2.erode(img, kernel = np.ones((5, 5), np.uint8))

contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contours:

    approx = cv2.approxPolyDP(i, 0.001 * cv2.arcLength(i, True), True)
    cv2.drawContours(img_bgr, [approx], 0, (0, 0, 255), 5)

    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
    i = 0
  
    font = cv2.FONT_HERSHEY_COMPLEX
    for j in n :
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string = str(x) + " " + str(y) 
  
            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(img, "Arrow tip", (x, y),
                                font, 0.5, (255, 0, 0)) 
            else:
                # text on remaining co-ordinates.
                cv2.putText(img_bgr, string, (x, y), 
                          font, 0.5, (0, 255, 0)) 
        i = i + 1

cv2.imshow('with contours', img_bgr)
cv2.waitKey(0)