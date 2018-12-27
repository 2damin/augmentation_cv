import cv2
import numpy as np
import os
import glob

path = "C:\\Users\\Damin\\Desktop\\saeronDeeplearning\\data\\addedData\\tmp"
imgNames = []

for i in os.listdir(path):
    tmp = path + "\\" + i
    imgNames.append(tmp)
print(imgNames)
#print(imgNames[0][77:-4])
#print(imgNames[0][79:80])
#os.system("pause")

for j in range(len(imgNames)):
    for fpath in glob.glob(imgNames[j]):
        #fpath_r = fpath.replace("_blur_", "_noise_")
        fpath_r = fpath.replace(".xml", "_reversal.xml")
        #fpath_r = fpath.replace(imgNames[j][70:],"_{}".format(j+23)+".xml")
        print(fpath_r)

        os.rename(fpath, fpath_r)






