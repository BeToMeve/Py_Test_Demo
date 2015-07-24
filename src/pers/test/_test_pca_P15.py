#coding:utf-8
'''
Created on 2015年7月24日

@author: Administrator
'''
from PIL import Image
from numpy import *
from pylab import *
import pca
from pers.test import imtools

imlist=imtools.get_imlist("D:/Python_workspace/pcv_data/data/fontimages/a_thumbs/")
im = array(Image.open(imlist[0])) #打开衣服图像，获取其大小
m,n = im.shape[0:2]#获取图像的大小
imnbr = len(imlist)#获取图像的数目
print imlist
#创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')

#执行PCA操作
V,S,immean = pca.pca(immatrix)

#显示一些图像（均值图像和前7个模式）
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()