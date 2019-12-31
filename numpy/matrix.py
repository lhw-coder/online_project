import numpy.matlib as mt
import numpy as np
"""
矩阵库
"""


a = mt.empty((3,4))
print(a,type(a))

b = mt.zeros((3,4))
print(b,type(b))

c = mt.ones((3,4))
print(c,type(c))

d = mt.eye(n=3,M=4,k=1,dtype=int)
print(d,type(d))

f = mt.identity(5,dtype=int)
print(f, type(f))

m = mt.matrix("1 2 3;4 5 6;7 8 9")
print(m,type(m))

aa = np.eye(2)
bb = aa * 2
cc = np.bmat("a b;b a")
print("c :\n", c)
