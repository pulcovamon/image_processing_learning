from cv2 import findContours
from matplotlib.pyplot import contour
import numpy as np
import cv2

img_bgr = cv2.imread(r'my_tryings\cells.png')

img = img_bgr[:,:,0]
_, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY + cv2. THRESH_OTSU)
# find coordinates of contours first: tompost vertex
contours, _ = findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contours:

    approx = cv2.approxPolyDP(i, 0.009 * cv2.arcLength(i, True), True)
    cv2.drawContours(img_bgr, [approx], 0, (0, 0, 255), 5)

cv2.imshow('with contours', img_bgr)
cv2.waitKey(0)