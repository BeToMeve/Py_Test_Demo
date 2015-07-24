#coding:utf-8
'''
Created on 2015年7月23日

@author: Administrator
'''
from PIL import Image
from pylab import *
'''
#读取图像到数组中
im = array(Image.open("C:\Users\Administrator\Desktop\empire.jpg"))

#绘制图像
imshow(im)

#一些点(X轴坐标，Y轴坐标)
x=[100,100,200,200]
y=[200,300,200,300]
#使用红色形状标记绘制点
plot(x,y,'r*')
plot(x,y)
#绘制链接前4个点的线
plot(x[:4],y[:4],'--c')
#添加标题，显示绘制的图像
title('Plotting :"empire.jpg"')
axis('off')#关闭不显示坐标轴
show()
'''
im=array(Image.open("C:\Users\Administrator\Desktop\empire.jpg").convert('L'))
#新建一个图像
figure()
#不适用颜色信息
gray()
#在原点的左上角显示轮廓图像
contour(im,origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()