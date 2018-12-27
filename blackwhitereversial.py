import cv2 as cv
import os, glob
import numpy as np

def imageShow(windowName, image, flags = cv.WINDOW_GUI_EXPANDED):
    cv.namedWindow(windowName, flags)
    cv.imshow(windowName,image)
    cv.waitKey(0)

path = "C:\\Users\\Damin\\Desktop\\saeronOCR\\ssd_mobilenet\\ssd_mobilenet\\test_data\\test_image\\histogrameq"

#originalPath = path + "\\original"
#reversalPath = path + "\\reversal"
originalPath = path

imageIn = []
for i in os.listdir(originalPath):
    print(i)
    imagePath = originalPath + "\\" + i
    imageIn.append(imagePath)

print("Total images : ", len(imageIn))

for i in range(len(imageIn)):
    image_ = cv.imread(imageIn[i], cv.IMREAD_GRAYSCALE)
    image_[:,:] = 245 - image_[:,:]
    cv.imwrite(imageIn[i], image_)
    if (i % 100 == 0):
        print(i, " 번째 작업중")

"""
    for fpath in glob.glob(imageIn[i]):
        fpath_r = fpath.replace(originalPath, reversalPath)
        fpath_r = fpath_r.replace(".png", "_reversal.png")
        fpath_r = fpath_r.replace(".PNG", "_reversal.PNG")
        #print(fpath_r)
"""

    #imageShow("window", image_)


