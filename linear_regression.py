import numpy as np
import cv2 as cv
import os
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
path="/Users/rihengzhu/Desktop/final_Riheng_Zhu/English/Hnd/Img/"
floder_lst=os.listdir(path)
train_labels=[]
test_labels=[]
test_matrix=[]
train_matrix=[]
image_matrix=[]
lables=[]
num=0
lst = [m for m in range(1,56)]
np.random.shuffle(lst)
print(0)
for floder_name in floder_lst:
    sub_floder=path+floder_name+"/"
    images=os.listdir(sub_floder)
    for image in images:
        a=sub_floder+image
        file = cv.imread(a, cv.IMREAD_GRAYSCALE)
        #file = cv.adaptiveThreshold(file, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY, 11, 2)
        #file = cv.resize(file,(90,120))
        file=file[100:800,300:1000]
        print(file.shape)
        cv.imshow('1',file)
        cv.waitKey(0)
        cv.destroyWindow()
        size=(int(110), int(90))
        out = cv.resize(file, size, interpolation=cv.INTER_AREA)
        kernel = np.ones((3, 3), np.float32) / 10

        file = cv.filter2D(file, -1, kernel)
        file=out.reshape(9900)

print(1)
