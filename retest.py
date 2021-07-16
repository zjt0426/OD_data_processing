import os

# a = 'D:\Desktop\GT\patch_xml\0000078_03810_d_0000011_0|0_0_768_768_3_1360_765.jpg'
#
# c = 'D:\Desktop\GT\label_xml'
# b = a.split('\\')[-1]
# b = '0000078_03810_d_0000011_0|0_0_768_768_3_1360_765.jpg'
# print(b)
# print(b[:-4])
# t = str(b[:-4] + '.xml')
# print(t)
# x = os.path.join(c,t)
# print(x)
#
# raw_images_dir = 'D:\Desktop\GT\oneimage'+'\\'  # 这里就是原始的图片

# print(raw_images_dir)
a = '/media/server/zjt00000/JEPGimage/0000078_03810_d_0000011_2.jpg'
b = a.split('/')[-1]
print(b)
root_dir = "/media/server/zjt00000/"
b = 'images_split' + '/'
image_dir = os.path.join(root_dir, b)
print(b)
print(image_dir)