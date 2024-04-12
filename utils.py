import os

root = '200_version'
txt_path = 'index.txt'
img_names = os.listdir(root)

# 补充某些无路径的图
for i in range(len(img_names)):
    if img_names[i].find('.') == -1:
        os.rename(os.path.join(root, img_names[i]), os.path.join(root, img_names[i]+'.jpg'))
        img_names[i] += '.jpg'       

# 构建一个索引txt
with open(txt_path, 'w') as f:
    for img_name in img_names:
        f.write(img_name + '\n')