# nefunguje!

from time import sleep
import cv2
import numpy as np

img = cv2.imread('planet.png')
for i in range(256):
    img = img - 1
    cv2.imshow('image', img)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()  
        break
