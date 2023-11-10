import os
os.getcwd()
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.image as mpimg
cv_img = cv2.imread('Plot6.jpg')
cv2.imshow('Plot6',cv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

