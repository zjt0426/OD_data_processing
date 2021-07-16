import glob
import os

# class_name = ['ignored regions', 'pedestrian', 'people','bicycle','car', 'van', 'truck', 'tricycle','awning-tricycle', 'bus','motor','others']
class_sort = {'pedestrian': 1, 'people': 2,'bicycle': 3,'car': 4, 'van': 5, 'truck': 6, 'tricycle': 7,'awning-tricycle': 8, 'bus': 9,'motor': 10}


path = 'D:\\Desktop\\Python\\data\\data_test-challenge_txt\\*'  # 得到的txt目录，以class为类别

# print(path)

save_path = r'D:\Desktop\Python\data\images_test-challenge_txt'   # 生成的visdrone类型的txt

txt_filenames = glob.glob(pathname=path)
for filename in txt_filenames:
    print(filename)  # 最后使用\来分割，并取最后一个字符串
    clc = filename.split("\\")[-1]
    print(clc)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            tem = line.strip("\n")
            # line.rstrip("\n")为去除行尾换行符
            # 差一个将读取所有文件的过程
            # tem = f.readline().strip("\n")
            # print(tem)
            tem_split = tem.split(' ')
            # print(tem_split)
            name = tem_split[0]
            print(name)
            x1 = tem_split[2]
            y1 = tem_split[3]
            x2 = tem_split[4]
            y2 = tem_split[5]

            width = float(x2) - float(x1) + 1.0
            length = float(y2) - float(y1) + 1.0
            conf = tem_split[1]
            print(float(x1), float(y1), width, length, conf, class_sort[clc])


            txt = open(save_path + '\\%s.txt' % name, 'a')
            new_box = [int(float(x1)), int(float(y1)), int(float(width)), int(float(length)), conf, class_sort[clc], -1, -1]

            txt.write(",".join([str(a) for a in new_box]))
            txt.write('\n')
            txt.close()



# print(txt_filenames)