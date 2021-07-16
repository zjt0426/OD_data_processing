import glob

res1, res2 = [], []
path_save = 'D:\\Desktop\\Python\\data\\images_test-challenge_txt\\*'   # 缺少的文件目录
save_path = r'D:\Desktop\Python\data\images_test-challenge_txt'      # 补全保存的文件目录

filename = glob.glob(pathname=path_save)

for file in filename:
    a = file.strip('.txt').split('\\')[-1]
    # print(a)
    res1.append(a)
    # print(res1)
    print(len(res1))
# path_save2 = 'D:\\Desktop\\Python\\data\\dataiccv\\VisDrone2019-DET-test-dev\\VisDrone2019-DET-test-dev\\annotations\\*'
path_save2 = 'D:\\Desktop\\Python\\data\\dataiccv\\VisDrone2019-DET-test-challenge\\VisDrone2019-DET-test-challenge\\images\\*'
# 原数据目录
filename = glob.glob(pathname=path_save2)

for i, file in enumerate(filename):
    b = file.strip('.jpg').split('\\')[-1]
    # print(b)
    # print(i)
    res2.append(b)
    # print(res2)
    print(len(res2))

for i in res2:
    if i not in res1:
        txt = open(save_path + '\\%s.txt' % i, 'a')
        txt.close()
        print(i)