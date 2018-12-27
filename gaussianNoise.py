from skimage import io, transform
import numpy as np
import cv2
import os, glob

def imageShow(imageName, image, flag=cv2.WINDOW_GUI_EXPANDED):
    cv2.namedWindow(imageName, flag)
    cv2.imshow(imageName, image)
    cv2.waitKey()

def brightChange(imgList, path, noise_sigma):
    for i in range(len(imgList)):
        print(i)
        np.random.seed(0)
        image = cv2.imread(imgList[i], cv2.IMREAD_GRAYSCALE)
        height, width = image.shape[:2]
        noise = np.random.randn(height, width) * noise_sigma
        for j in range(height):
            for k in range(width):
                image[j, k] += noise[j, k]

        print(imgList[0])
        os.system("pause")
        for fpath in glob.glob(imgList[i]):
            # fpath_r = fpath.replace(imgNames[j][79:80], "_sobel_"+"{}".format(index))
            fpath_r = fpath.replace("_", "_noise_")
            fpath_r = fpath_r.replace("original", "noise")

        print(fpath_r)
        cv2.imwrite(fpath_r, image)

    print("bright changing done")

def add_gaussian_noise(image_in, noise_sigma):
    for i in range(len(image_in)):
        imageRead = cv2.imread(image_in[i], cv2.IMREAD_GRAYSCALE)

        h = imageRead.shape[0]
        w = imageRead.shape[1]
        noise = np.random.randn(h, w) * noise_sigma

        if len(imageRead.shape) == 2:
            for j in range(h):
                for k in range(w):
                    imageRead[j,k] += noise[j,k]
        else:
            for j in range(h):
                for k in range(w):
                    imageRead[j, k, 0] += noise[j, k]
                    imageRead[j, k, 1] += noise[j, k]
                    imageRead[j, k, 2] += noise[j, k]

        for fpath in glob.glob(image_in[i]):
            #fpath_r = fpath.replace(imgNames[j][79:80], "_sobel_"+"{}".format(index))
            fpath_r = fpath.replace("_", "_noise_")
            fpath_r = fpath_r.replace("original", "noise")

        print(fpath_r)
        cv2.imwrite(fpath_r, noisy_image)
    print("bright changing done")


path = "C:\\Users\\Damin\\Desktop\\saeronDeeplearning\\data\\addedData\\fontdata2\\data\\ikltuvw"
originalDir = path + "\\original"
imgNames = []
for i in os.listdir(originalDir):
    imageName = originalDir +"\\"+ i
    imgNames.append(imageName)

print(imgNames)

noise_sigma = 5
#brightChange(imgNames, path, noise_sigma)
add_gaussian_noise(imgNames, noise_sigma)




