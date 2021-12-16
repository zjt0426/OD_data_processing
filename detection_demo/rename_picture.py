
import cv2
import os

path = r'D:\dessktop\faces'

imgs_list = os.listdir(path)

for i, image in enumerate(imgs_list):
    img_path = path+'\\'+image
    print(img_path)
    print(image)
    img = cv2.imread(img_path)
    # cv2.imshow('image1', img)
    # cv2.waitKey(0)
    print(i)
    cv2.imwrite((path + '\\' + '%s.jpg') % i, img)