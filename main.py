from scan_path import *
from get_creation_date import *

mypath=r"E:\My Files"
sf, doc_files, img_files, oth_files = scan_path(mypath)

for i in img_files:
    print(creation_date(i))

# path_to_file = r"E:\My Files\2020-07-08 10_40_10-Window.jpg"
# local_time = creation_date(path_to_file)








