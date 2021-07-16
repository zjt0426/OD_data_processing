import os



root_dir = r"E:\My__Desktop\virdata\VisDrone2019-DET-train\VisDrone2019-DET-train"
# annotations_dir = root_dir+"annotations"
a = 'annotations' + "\\"
print(a)
annotations_dir = os.path.join(root_dir, a)
print(annotations_dir)