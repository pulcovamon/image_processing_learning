import cv2
import numpy as np
  
# Open the image.
img = cv2.imread('low_contrast.png')
  
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
      
    # Apply gamma correction.
    img_gamma = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
  
    cv2.imshow('img', img_gamma)
    cv2.waitKey(0)

cv2.destroyAllWindows()