import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')

size = img.shape[0:2]
print(size)
size_bigger = (size[1] * 10, size[0] * 10)
print(size_bigger)

img_half = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
img_bigger = cv2.resize(img, (size_bigger))              # resize function follows the order (width, height) instead of (height, width)
img_stretch_near = cv2.resize(img, (size_bigger), interpolation = cv2.INTER_NEAREST)  
print(img_stretch_near.shape)

titles = ['orig', 'half', 'bigger', 'interp']
images = [img, img_half, img_bigger, img_stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])

plt.show()