import cv2
import numpy as np
import os
import pandas
import glob

def imageRead(openpath, flag=cv2.IMREAD_UNCHANGED):
    image = cv2.imread(openpath, flag)
    if image is not None:
        print("Image Opened")
        return image
    else:
        print("Image Not Opened")
        print("Program Abort")
        exit()


def imageShow(imagename, image, flag=cv2.WINDOW_GUI_EXPANDED):
    cv2.namedWindow(imagename, flag)
    cv2.imshow(imagename, image)
    cv2.waitKey()


def sobelEdge(image, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=3):
    return cv2.Sobel(image, ddepth, dx, dy, ksize=ksize)


def addImage(image1, image2):
    return cv2.add(image1, image2)

path = "C:\\Users\\Damin\\Desktop\\saeronOCR\\ssd_mobilenet\\ssd_mobilenet\\test_data\\test_image\\histogrameq"
imgNames = []

#originalImage_path = path + "\\original"
originalImage_path = path

for i in os.listdir(originalImage_path):
    tmp = originalImage_path + "\\" + i
    imgNames.append(tmp)

print(imgNames)

for i in range(len(imgNames)):
    print(i)
    roadColor = imageRead(imgNames[i], cv2.IMREAD_COLOR)
    # imageShow("roadColor", roadColor)

    roadColor_Sobel_x = sobelEdge(roadColor, cv2.CV_8U, 1, 0, 1)
    #imageShow("roadColor_Sobel_x", roadColor_Sobel_x)

    roadColor_Sobel_y = sobelEdge(roadColor, cv2.CV_8U, 0, 1, 1)
    #imageShow("roadColor_Sobel_y", roadColor_Sobel_y)

    roadColor_Sobel_x_and_y = addImage(roadColor_Sobel_x, roadColor_Sobel_y)
    #imageShow("roadColor_Sobel_x_and_y", roadColor_Sobel_x_and_y)

    for fpath in glob.glob(imgNames[i]):
        #fpath_r = fpath.replace(imgNames[j][79:80], "_sobel_"+"{}".format(index))
        fpath_r = fpath.replace("_","_sobel_")
        fpath_r = fpath_r.replace("original", "sobel")
        #fpath_r = fpath_r.replace("sobel_aug", "aug")

    print(fpath_r)
    #os.system("pause")
    cv2.imwrite(imgNames[i], roadColor_Sobel_x_and_y)

    #cv2.imwrite(imgNames[i],roadColor_Sobel_x_and_y)


#roadColor_Sobel = sobelEdge(roadColor, cv2.CV_8U, 1, 1, 3)
#imageShow("roadColor_Sobel", roadColor_Sobel)

cv2.destroyAllWindows()