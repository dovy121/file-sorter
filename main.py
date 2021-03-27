import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

doc_ext = [".doc", ".docx", ".txt"]
img_ext = [".png", ".jpeg", ".jpg", ".bmp"]

sort_path = input("Please place path which will be used to sort in: ")
item_list = os.listdir(sort_path)

for item in item_list:
    file = sort_path +"\\"+item
    if os.path.isdir(file):
       os.mkdir(sort_path + "\\Folders")
       shutil.move(file, sort_path + "\\Folders\\" + item)
    if os.path.isfile(file)
        #need to finish here








print(new_list)


