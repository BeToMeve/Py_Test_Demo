#coding:utf-8
'''
Created on 2015年7月23日

@author: Administrator
'''
from numpy import *
from PIL import Image
from matplotlib.pyplot import imshow
from ImageShow import show

# im=array(Image.open("C:\Users\Administrator\Desktop\empire.jpg"))
# print im.shape,im.dtype
#  
# im=array(Image.open("C:\Users\Administrator\Desktop\empire.jpg").convert('L'),'f')
# print im.shape,im.dtype

im=array(Image.open("C:\Users\Administrator\Desktop\empire.jpg").convert('L'))

im2=255-im#对图像进行反相处理
pil_im=Image.fromarray(im)
im3=(100.0/255)*im+100#将图像像素值变换到100。。。200区间

im4=255.0*(im/255.0)**2#对图像像素值求平方后得到的图像

print int(im.min()),int(im.max())
print int(im2.min()),int(im2.max())
# print int(pil_im.min()),int(pil_im.max())
print int(im3.min()),int(im3.max())
print int(im4.min()),int(im4.max())