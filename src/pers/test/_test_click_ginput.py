#coding:utf-8
'''
Created on 2015年7月23日

@author: Administrator
'''
from PIL import Image
from pylab import *

im=array(Image.open("C:\Users\Administrator\Desktop\empire.jpg"))
imshow(im)
print 'Please click 3 points'
x=ginput(3)
print 'you clicked :'
for i in x:
    for j in i:
        j=int(j)
        print j
        print i
print x
show()