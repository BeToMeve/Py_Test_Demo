# -*- coding: utf-8 -*-
#  coding=utf-8
##输入半径求面积
# pi = 3.14
# radius = float(raw_input("Radius:"))
# area = pi * radius**2
# print area
# x=int(raw_input(""))
# print x

# 
# import os 
#   
# dirpath="D:\Python_workspace"
# for fname in os.listdir(dirpath): 
#     newfname=fname[3:] 
#     newfpath="%s/%s"%(dirpath,newfname) 
#     oldfpath="%s/%s"%(dirpath,fname) 
#       
#     os.rename(oldfpath, newfpath)

# coding=utf-8 
''' 
import os 
import re 
  
path = "D:\Python_workspace"
pattern = re.compile('d{3}') 
  
for file in os.listdir(path): 
    if os.path.isfile(os.path.join(path, file)): 
        match = pattern.search(file) 
        assert match 
        name = match.group() + '.mp3'
        #print file, name 
        os.rename(os.path.join(path, file), os.path.join(path, name))
'''

from PIL import Image
from pylab import *
pil_im = Image.open("C:\Users\Administrator\Desktop\empire.jpg")
pil_im=pil_im.convert('L')
'''
pil_im.thumbnail((64,64))#创建最长边为128的缩略图
'''
'''
#选取方块旋转180度
box = (100,100,400,400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
'''
out = pil_im.resize((128,128))#缩放到新的尺寸128*128
out = pil_im.rotate(45)#旋转45度
imshow(out)
show()