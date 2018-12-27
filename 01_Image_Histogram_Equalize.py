import cv2
import numpy as np
import os
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


def splitImageByCV(image):
    return cv2.split(image)


def mergeImageByCV(channel1, channel2, channel3):
    return cv2.merge((channel1, channel2, channel3))


def convertColor(image, flag=None):
    if flag is None:
        return image
    else:
        return cv2.cvtColor(image, flag)


def histogramEqualize(image):
    return cv2.equalizeHist(image)


path = "C:\\Users\\Damin\\Desktop\\saeronOCR\\ssd_mobilenet\\ssd_mobilenet\\test_data\\test_image\\histogrameq"
imgNames = []

originalImage_path = path
for i in os.listdir(originalImage_path):
    tmp = originalImage_path + "\\" + i
    imgNames.append(tmp)


for i in range(len(imgNames)):
    print(i)
    #roadColor = imageRead(imgNames[i], cv2.IMREAD_COLOR)
    grayColor = imageRead(imgNames[i], cv2.IMREAD_GRAYSCALE)

    "grayColor histogram equalization"
    """
    grayColor_equalized = histogramEqualize(grayColor)
    cv2.imwrite(imgNames[i], grayColor_equalized)
    """

    """
    b, g, r = splitImageByCV(roadColor)
    #imageShow("b", b)
    #imageShow("g", g)
    #imageShow("r", r)

    b_Equalize = histogramEqualize(b)
    #imageShow("b_Equalize", b_Equalize)
    g_Equalize = histogramEqualize(g)
    #imageShow("g_Equalize", g_Equalize)
    r_Equalize = histogramEqualize(r)
    #imageShow("r_Equalize", r_Equalize)

    roadColor_Equalized = mergeImageByCV(b_Equalize, g_Equalize, r_Equalize)
    """


    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
    claheImg = clahe.apply(grayColor)
    #imageShow("roadColor_Equalized_By_Channels", claheImg)

    
    for fpath in glob.glob(imgNames[i]):
        #fpath_r = fpath.replace(imgNames[j][79:80], "_sobel_"+"{}".format(index))
        fpath_r = fpath.replace("_","_histo_")
        fpath_r = fpath_r.replace("original", "histo")
        #fpath_r = fpath_r.replace("histo_aug", "aug")

    cv2.imwrite(imgNames[i], claheImg)
    #cv2.imwrite(path + "\\histogramEq2\\" + "1_08168E_histo_{}".format(i)+".png", claheImg)



    """HSV Equalization"""
    #hsv = convertColor(roadColor, cv2.COLOR_BGR2HSV)
    #imageShow("hsv", hsv)

    #h, s, v = splitImageByCV(hsv)
    #imageShow("h", h)
    #mageShow("s", s)
    #imageShow("v", v)

    #h_Equalize = histogramEqualize(h)
    #imageShow("h_Equalize", h_Equalize)
    #s_Equalize = histogramEqualize(s)
    #imageShow("s_Equalize", s_Equalize)
    #v_Equalize = histogramEqualize(v)
    #imageShow("v_Equalize", v_Equalize)

    #hsv_Equalized = mergeImageByCV(h_Equalize, s_Equalize, v_Equalize)
    #hsv_Equalized = convertColor(hsv_Equalized, cv2.COLOR_HSV2BGR)
    #imageShow("hsv_Equalized", hsv_Equalized)

    #sv_Equalized = mergeImageByCV(h, s_Equalize, v_Equalize)
    #sv_Equalized = convertColor(sv_Equalized, cv2.COLOR_HSV2BGR)
    #imageShow("sv_Equalized", sv_Equalized)

    #s_Only_Equalized = mergeImageByCV(h, s_Equalize, v)
    #s_Only_Equalized = convertColor(s_Only_Equalized, cv2.COLOR_HSV2BGR)
    #imageShow("s_Only_Equalized", s_Only_Equalized)

    #v_Only_Equalized = mergeImageByCV(h, s, v_Equalize)
    #v_Only_Equalized = convertColor(v_Only_Equalized, cv2.COLOR_HSV2BGR)
    #imageShow("v_Only_Equalized", v_Only_Equalized)


cv2.destroyAllWindows()