# coding: utf-8  
import os   
FindPath="D:\Python_workspace"  
filenames=os.listdir(FindPath)   
for name in filenames:  
    filePath=os.path.join(FindPath,name)  
    print(filePath)
print"sss",filePath
print(filenames)