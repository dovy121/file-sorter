import os
import platform
import glob
import datetime
import os.path, time
import shutil

my_path = r"E:\test"

# sf, doc_files, img_files, oth_files = scan_path(my_path)
items = glob.glob(my_path + r'\*', recursive=False)

# print "last modified: %s" % time.ctime(os.path.getmtime(file))


def creation_date(path_to_file):
    if platform.system() == 'Windows':
        created = datetime.fromtimestamp(getctime(path)).strftime('%d %b %Y, %H:%M:%S')
        return time.ctime(os.path.getctime(path_to_file))

    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def is_dir(path):
    if os.path.isdir(path):
        return True


def is_doc(path):
    doc_ext = [".doc", ".docx", ".txt", ".pdf", ".txt", ".xls", ".xlsx", ".ods", ".ppt", ".pptx"]
    if os.path.isfile(path) and os.path.splitext(path)[1].lower() in doc_ext:
        return


def is_img(path):
    img_ext = [".png", ".jpeg", ".jpg", ".bmp", ".gif", ".raw", ".tiff", ".tif", ".eps"]
    if os.path.isfile(path) and os.path.splitext(path)[1].lower() in img_ext:
        return


def is_vid(path):
    vid_ext = [".mp4", ".avi", ".flv", ".mov", ".ogg", ".m4p", ".wmv", ".swf", ".m4v"]
    if os.path.isfile(path) and os.path.splitext(path)[1].lower() in vid_ext:
        return


def is_arc(path):
    arc_ext = [".zip", ".7z", ".rar", ".tar"]
    if os.path.isfile(path) and os.path.splitext(path)[1].lower() in arc_ext:
        return


for i in items:
    # gives the create time as a unix timestamp
    create_time = os.stat(i).st_ctime
    # returns a datetime object
    create_datetime = datetime.datetime.fromtimestamp(create_time)
    file_year = create_datetime.strftime("%Y")
    if not os.path.exists(my_path + "\\" + file_year):
        os.makedirs(my_path + "\\" + file_year)
        print(f"... Created folder: {my_path}\\{file_year}")

    if is_dir(i):
        target = r'target path where the directory will be moved\directory name'
        os.path.splitext(path)[1].lower()
        shutil.move(original, target)


