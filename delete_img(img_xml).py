import os

# folder_path =input("Enter The PATH: ")
folder_path = r"D:\Bag_labeling\hhb\w_l2_morning_frames"
files = os.listdir(folder_path)
print('total files: ', len(files), '\n')

xmls_name = []
images = []
for file in files:
    exe = file.split('.')[-1]
    if exe == 'png' or exe == 'jpg' or exe == 'jpeg':
        images.append(file)
    elif exe == 'xml':
        xmls_name.append(os.path.splitext(file)[0])

print('xmls: ', len(xmls_name))
print('images: ', len(images), '\n')

for img in images:
    if os.path.splitext(img)[0] not in xmls_name:
        os.remove(os.path.join(folder_path, img))

print('done')
