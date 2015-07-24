#coding:utf_8
'''
Created on 2015Äê7ÔÂ24ÈÕ

@author: Administrator
'''
from PIL import Image
from numpy import *
from pylab import *

# im = array(Image.open('2_t.jpg'))
# m,n = im.shape[0:2]
# print im,m,n
# imatrix = array([im.flatten()])
# print imatrix
A=np.array([[1,2,3],[1,2,3]],dtype = int)
m,n=shape(A)
B=np.eye(3, 3,dtype='int')
print A,m,n,B
help(shape)