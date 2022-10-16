import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('monkey.jpg')


#cv2.imshow('image', img)
#cv2.waitKey(0)

plt.imshow(img)
plt.show()

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(rgb_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

path = r'monkey.jpg'
img = cv2.imread(path, 0) # 0 for reading image in grayscale mode
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows

print(img.shape)