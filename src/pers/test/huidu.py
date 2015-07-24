#coding:utf-8
from PIL import Image
from numpy import *
from ImageShow import show
from matplotlib import *
from pylab import *

im = array(Image.open("C:\Users\Administrator\Desktop\empire.jpg").convert('L'))

im2=255-im#对图像进行反相处理

im3=(100.0/255)*im+100#将图像像素值变换到100。。。200区间

im4=255.0*(im/255.0)**2#对图像像素值求平方后得到的图像
im5=Image.open("C:\Users\Administrator\Desktop\empire.jpg")
print int(im.min()),int(im.max())
print '11'
# imshow(im)
# imshow(im2)
# imshow(im3)
imshow(im4)
show()