import os
os.getcwd()
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as mpimg
cv2.namedWindow("output",cv2.WINDOW_NORMAL)
cv_img = cv2.imread('Plot6.jpg')
cv_img= cv2.resize(cv_img,(960,540))
cv_img_hsv = cv2.cvtColor(cv_img,cv2.COLOR_BGR2HSV)
#light green
hsv_color1 = np.asarray([0,128,0])  
#green // 170 255 0
hsv_color2 = np.asarray([144,238,144])
mask = cv2.inRange(cv_img_hsv,hsv_color1,hsv_color2)
plt.imshow(mask,cmap='gray')
plt.show()



