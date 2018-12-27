import cv2
import numpy as np


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


def cannyEdge(image, threshold1=100, threshold2=200):
    return cv2.Canny(image, threshold1, threshold2)


def nothing(x):
    pass

#path = "../../Data/"
path = "C:\\Users\\Damin\\Desktop\\saeronOCR\\ssd_mobilenet\\ssd_mobilenet\\test_data\\test_image\\histogrameq"
roadImage = "\\4.png"

openPath = path+roadImage

roadColor = imageRead(openPath, cv2.IMREAD_GRAYSCALE)
backup = np.copy(roadColor)
cv2.namedWindow('image', cv2.WINDOW_GUI_EXPANDED)

roadColor = cannyEdge(backup, 25, 75)
cv2.imwrite(path +"\\4_canny.png", roadColor)
cv2.imshow('image', roadColor)
cv2.waitKey(0)

cv2.destroyAllWindows()