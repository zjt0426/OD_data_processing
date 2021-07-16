from __future__ import division
import os
from PIL import Image
from xml.dom import minidom
# import xml.dom.minidom
import numpy as np

ImgPath = r'D:\Desktop\GT\image'
AnnoPath = r'D:\Desktop\GT\label'
ProcessedPath = r'D:\Desktop\GT\patch_xml'

prefix_str = '''<annotation>
	<folder>VOC2007</folder>
	<filename>{}.jpeg</filename>
	<source>
		<database>The VOC2007 Database</database>
		<annotation>Ring Cell Dataset</annotation>
		<image>flickr</image>
	</source>
	<size>
		<width>2003</width>
		<height>2010</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>'''

suffix = '</annotation>'

new_head = '''	<object>
		<name>head</name>
		<bndbox>
			<xmin>{}</xmin>
			<ymin>{}</ymin>
			<xmax>{}</xmax>
			<ymax>{}</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>'''
imagelist = os.listdir(ImgPath)
for image in imagelist:
    image_pre, ext = os.path.splitext(image)  # 将图片的名称拆成两部分，名称和图片格式
    imgfile = ImgPath + '\\' + image
    xmlfile = AnnoPath + '\\' + image_pre + '.xml'

    # DomTree = xml.dom.minidom.parse(xmlfile)  # 打开xml文档
    DomTree = minidom.parse(xmlfile)  # 打开xml文档
    annotation = DomTree.documentElement  # 得到xml文档对象

    filenamelist = annotation.getElementsByTagName('filename')  # [<DOM Element: filename at 0x381f788>]
    filename = filenamelist[0].childNodes[0].data  # 获取XML节点值
    namelist = annotation.getElementsByTagName('name')
    objectname = namelist[0].childNodes[0].data
    savepath = ProcessedPath + objectname
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    bndbox = annotation.getElementsByTagName('bndbox')
    b = bndbox[1]
    print(b.nodeName)
    i = 1
    # a = [0, 300, 0, 300]
    # b = [0, 0, 300, 300]
    a = [0, 680, 0, 680]
    b = [0, 0, 382, 382]
    h = 382
    cropboxes = []


    def select(m, n):
        bbox = []
        for index in range(0, len(bndbox)):
            x1_list = bndbox[index].getElementsByTagName('xmin')  # 寻找有着给定标签名的所有的元素
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = bndbox[index].getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = bndbox[index].getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = bndbox[index].getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            print("the number of the box is", index)
            print("the xy", x1, y1, x2, y2)
            if x1 >= m and x2 <= m + h and y1 >= n and y2 <= n + h:
                print(x1, y1, x2, y2)
                a1 = x1 - m
                b1 = y1 - n
                a2 = x2 - m
                b2 = y2 - n
                bbox.append([a1, b1, a2, b2])  # 更新后的标记框
        if bbox is not None:
            return bbox
        else:
            return 0


    cropboxes = np.array(
        [[a[0], b[0], int(a[0] + 1.8 * h), int(b[0] + 1.2 * h)], [a[1]-50, b[1], int(a[1] + 1.8 * h), int(b[1] + 1.2 * h)], [a[2], b[2]-50, int(a[2] + 1.78 * h), b[2] + h],
         [a[3]-50, b[3]-50, int(a[3] + 1.78 * h), b[3] + h]])
    # cropboxes = np.array(
    #     [[0,0,544,280],[408,0,952,280],[816,0,1360,280],[0,250,544,520],[408,250,952,520],[816,250,1360,520],[0,495,544,765],[408,495,544,765],[816,495,1360,765]]
    # )
    img = Image.open(imgfile)
    for j in range(0, len(cropboxes)):
        print("the img number is :", j)
        Bboxes = select(a[j], b[j])
        if Bboxes is not 0:
            head_str = ''
            for Bbox in Bboxes:
                head_str = head_str + new_head.format(Bbox[0], Bbox[1], Bbox[2], Bbox[3])
        cropedimg = img.crop(cropboxes[j])
        xml = prefix_str.format(image) + head_str + suffix
        cropedimg.save(savepath + '/' + image_pre + '_' + str(j) + '.jpg')
        open(AnnoPath + 'test{}.xml'.format(j), 'w').write(xml)