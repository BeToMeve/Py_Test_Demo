#coding:utf-8
'''
Created on 2015��7��23��

@author: Administrator
'''
from PIL import Image
from numpy import *

def pca(X):
    """���ɷַ�����
        ���룺����X�����иþ����д���ѵ����ݣ�ÿһ��Ϊһ��ѵ�����
        ���أ�ͶӰ���󣨰���γ�ȵ���Ҫ�����򣩡�����;�ֵ
    """
    #��ȡά��
    num_data,dim=X.shape
    
    #������Ļ�
    mean_X=X.mean(axis=0)
    X=X-mean_X
    
    if dim>num_data:
        #PAC-ʹ�ý��¼���
        M = dot(X,X.T)#Э�������
        e,EV=linalg.eigh(M)#����ֵ����������
        tmp = dot(X.T,EV).T #����ǽ��¼���
        V = tmp[::-1] #����������������ʹ��������Ҫ�ģ�������Ҫ������ת
        S = sqrt(e)[::-1]#��������ֵ�ǰ��յ���˳�����еģ�������Ҫ������ת
        for i in range(V.shape[1]):
            V[:,i]/=S
    else:
        #PCA-ʹ��SVD����
        U,S,V=linalg.svd(X)
        V = V[:num_data] #��������num_dataά����ݲź���
        
    #����ͶӰ���󡢷���;�ֵ
    return V,S,mean_X