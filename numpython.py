# -*- coding: UTF-8 -*-

import numpy as np
from numpy import *

#create Array 创建数组

a = np.array([[1, 2, 3], [4, 5, 7]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

#special array 特殊数组
b = np.zeros((2,3))
d = np.ones((2,3))
f = np.empty((3,2))
print(b)
print(d)
print(f)

#sequence array 序列数组

print(np.arange(1,20,5))
print(np.linspace(0,2,9))

# index array  数组索引

g = np.array([[1,2,3,4],[5,4,6,8]])
#a = g[0]
print(g[0])


#数组运算

h = np.array([1,2,3])
j = np.array([4,5,6])
k = h + j
print(k)

#数组拷贝

l = np.ones((2,4))

m = l
print(m)

n = l.copy()

print(n)


#矩阵

#创建矩阵

p = np.matrix([[1.0,2.0],[3.0,4.0]])
q = np.matrix([[5.0,6.0],[7.0,8.0]])
print(p)
print(type(p))
print(q)
print(p * q)
print(p.I)





















