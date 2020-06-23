


import os, shutil


def stu_activities():

   
    for root, dirs, files in os.walk(os.path.expanduser("~/Downloads")):
        for file_name in files:
            if 'Stu_' in file_name:
            
    
                shutil.copy(os.path.join(root, file_name), os.getcwd())

stu_activities()
