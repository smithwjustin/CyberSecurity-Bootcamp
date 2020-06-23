
import os, shutil 


def pdf_copy():

   
    destination = os.getcwd()
    
    downloads = os.path.expanduser("~/Downloads")
    

    os.chdir(downloads)
    
    source = os.listdir(downloads)
    
    for files in source:
        print(files)
   
        if files.endswith("pdf") or files.endswith("docs"):
           
            shutil.copy(files,destination)
        
            print("-----")
pdf_copy()
