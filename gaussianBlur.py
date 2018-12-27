import numpy as np
import cv2
import os
import glob

path = "C:\\Users\\Damin\\Desktop\\saeronOCR\\ssd_mobilenet\\ssd_mobilenet\\test_data\\test_image\\histogrameq"
imgNames = []

#originalImage_path = path + "\\original"
originalImage_path = path

#폴더 내 파일 이름 다 불러와서 imgNames에 넣는다.
for i in os.listdir(originalImage_path):
    tmp = originalImage_path + "\\" + i
    imgNames.append(tmp)

print(imgNames)


for i in range(len(imgNames)):
    print(i)
    img = cv2.imread(imgNames[i], cv2.cv2.IMREAD_UNCHANGED)

    #medianimg = cv2.medianBlur(img, 9)
    #bilatimg = cv2.bilateralFilter(img, 7, 9, 9)

    gaussian = cv2.GaussianBlur(img, (7,7), 1,0,4)
    #cv2.imshow("gaussian", gaussian)
    #cv2.waitKey()

    #path 이름 변경
    for fpath in glob.glob(imgNames[i]):
        #fpath_r = fpath.replace(imgNames[j][79:80], "_sobel_"+"{}".format(index))
        fpath_r = fpath.replace("_","_blur_")
        fpath_r = fpath_r.replace("original", "blur")
        #fpath_r = fpath_r.replace("blur_aug", "aug")

    print(fpath_r)
    #os.system("pause")
    cv2.imwrite(imgNames[i], gaussian)

cv2.destroyAllWindows()
print("done")