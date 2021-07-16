from PIL import Image
import matplotlib.pyplot as plt
import os

# 定义待批量裁剪图像的路径地址
IMAGE_INPUT_PATH = 'D:\Desktop\GT\image'
# 定义裁剪后的图像存放地址
IMAGE_OUTPUT_PATH = 'D:\Desktop\GT\patch'


def image_cut(discard_upper_edge, discard_left_edge, discard_right_edge, discard_lower_edge, m, n, cell_weight,
              cell_height):
    # discard_upper_edge,discard_left_edge,discard_right_edge,discard_lower_edge分别是切小块前感兴趣区域的上下左右边界；
    # m是横向分割的块数，n是纵向分割的块数，cell_weight,cell_height分成的小块的长和宽

    # 每个图像全路径
    for each_image in os.listdir(IMAGE_INPUT_PATH):
        # 每个图像全路径
        image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
        with Image.open(image_input_fullname) as img:
            x1 = discard_left_edge  # 左边缘
            y1 = discard_upper_edge  # 上边缘
            x2 = discard_right_edge  # 右边缘
            y2 = discard_lower_edge  # 下边缘
            print(img.format, img.size, img.mode)
            # 每个图像截取的roi，roi是一个矩阵
            roi = img.crop((x1, y1, x2, y2))

            plt.imshow(roi)
            plt.axis('off')
            plt.show()

            print('it is ok')
            # image_output_roi = IMAGE_OUTPUT_PATH + "/roi_cut/" + each_image
            image_output_roi = IMAGE_OUTPUT_PATH + each_image
            # roi.save(image_output_roi)   # 可以选择不保存图片的感兴趣区域
            roi_w0 = x2 - x1
            roi_h0 = y2 - y1
            step_w = (m * cell_weight - roi_w0) / (m - 1)
            step_h = (n * cell_height - roi_h0) / (n - 1)
            t = 0
            for i in range(n):
                for j in range(m):
                    # crop(x1,y1,x2,y2)函数需要的参数是xoy坐标参数，与矩roi的矩阵(i,j)取值方法不同
                    region = roi.crop((j * (cell_weight - step_w), i * (cell_height - step_h),
                                       (j + 1) * cell_weight - j * step_w, (i + 1) * cell_height - i * step_h))
                    # 裁剪部分保存路径
                    image_output_fullname = IMAGE_OUTPUT_PATH + "/" + each_image
                    # image_output_cut_region_name = image_output_fullname.split(".")[0] + "_"+str(t+1)+"_"+str(i+1)+"_"+str(j+1)+"." + image_output_fullname.split(".")[-1]
                    image_output_cut_region_name = image_output_fullname.split(".")[0] + "_" + str(t + 1) + "_" + str(
                        i + 1) + "_" + str(j + 1) + ".png"
                    t += 1
                    # 保存图片
                    region.save(image_output_cut_region_name)
            print(step_w, step_h)
            print("{} crop done.".format(each_image))
            plt.close('all')
            plt.clf()


image_cut(0, 0, 1360, 765, 3, 2, 1024, 640)
# 前面四个表示感兴趣区域，可以设置为整张图片大小，接着两个值为横和竖的分割块，最后的为分成小块的大小608。