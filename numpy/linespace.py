"""
线性代数
"""
import numpy.matlib
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
# 矩阵乘法
print(np.dot(a,b))
# 矩阵对应位置相乘求和
print(np.vdot(a,b))
# 一维数组内积
print(np.inner(np.array([1,2,3]), np.array([0,1,0])))
# 多维是对应每一维相乘求和
print(np.inner(a,b))

# 求行列式
print(np.linalg.det(np.array([[1,2],[3,4]])))
print(np.linalg.det(np.array([[6,1,1],[4,-2,5],[2,8,7]])))

# 求矩阵的逆

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print(y)
print(np.dot(x,y))

# 求方程的解
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
ainv = np.linalg.inv(a)
print(ainv)
b = np.array([[6],[-4],[27]])
xx = np.linalg.solve(a,b)
print(xx)

# 求矩阵的秩
print(np.transpose(x))   # 转置
print(np.linalg.matrix_rank(x))

