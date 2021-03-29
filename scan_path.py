import os
import glob

def scan_path(path):

    sf, doc_files, img_files, vid_files, arc_files ,oth_files = [], [], [], [], [], []
    doc_ext = [".doc", ".docx", ".txt", ".pdf", ".txt", ".xls", ".xlsx", ".ods", ".ppt", ".pptx"]
    img_ext = [".png", ".jpeg", ".jpg", ".bmp", ".gif", ".raw", ".tiff", ".tif", ".eps"]
    vid_ext = [".mp4", ".avi", ".flv", ".mov", ".ogg", ".m4p", ".wmv", ".swf", ".m4v"]
    arc_ext = [".zip", ".7z", ".rar", ".tar"]
    items = glob.glob(path + r'\**\*', recursive=True)
    for f in items:
        if os.path.isdir(f):
            sf.append(f)
        if os.path.isfile(f):
            if os.path.splitext(f)[1].lower() in doc_ext:
                doc_files.append(f)
            elif os.path.splitext(f)[1].lower() in img_ext:
                img_files.append(f)
            elif os.path.splitext(f)[1].lower() in vid_ext:
                vid_files.append(f)
            elif os.path.splitext(f)[1].lower() in arc_ext:
                arc_files.append(f)
            else: oth_files.append(f)

    return sf, doc_files, img_files, oth_files