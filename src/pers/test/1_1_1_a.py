#coding: utf-8
'''
Created on 2015年7月23日

@author: Administrator
'''
from PIL import Image
import os
from _imaging import outline

FindPath="D:\\Python_workspace"
filelist=os.listdir(FindPath) 
# filenames=os.listdir(FindPath)   
# for name in filenames:  
#     filelist=os.path.join(FindPath,name) 
# print filelist
# filelist = "D:\Python_workspace"
for infile in filelist:
#     print os.path.splitext(infile)[0]+".jpg"
    outfile = os.path.splitext(infile)[0]+".jpg"
    print outfile
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            os.rename(infile,outline)
        except IOError:
            print "Cannot convert",infile