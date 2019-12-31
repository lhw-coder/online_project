import numpy as np
import random

"""
增
"""
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[10, 20], [30, 40], [50, 60]])
# 纵向合并
arr = np.vstack((a, b))
# print(arr)
# 纵向拆分
arr1 = np.vsplit(arr,3)
# print(arr1)
# for i in arr1:
#     print(i)
# 横向合并
arr2 = np.hstack((a,b))
# 横向拆分
arr3 = np.hsplit(arr2, 2)
# print(arr2, arr3)
# print(type(arr3))
"""
查
"""
# print(a[0])
# print(a[0][1])
# print(a[0,1])

cond = np.array([True,False,True,False])
a = np.where(cond,-2,2)# [-2 2 -2 2]
# print(a)

"""
删除
"""

d = np.array([[1, 2], [3, 4], [5, 6]])
f = np.delete(d, 1, axis=0)
# print(f)
g = np.delete(d, 1, axis=1)
# print(g)

"""
切片 高维数组

array切片都不会拷贝，切片就是原array的一个视图，就更谈不上深浅拷贝了
"""
ar = np.arange(15).reshape(3, 5)
# print(ar)
# print(ar[1,2], type(ar[1,2]))
# print(ar[0], type(ar[0]))
# 按横纵坐标找值
# print(ar[1,2])
# 多维切片
# print(ar[1:,1:4:2], type(ar[1:,1:4]))


"""
array 变为 list
"""
ar.tolist(), type(ar.tolist())


"""
bool型索引

把二维数组中的数值等于6的数改为5
"""
arr = np.arange(10).reshape((2,5))
arr[0][0] = 6
# print(arr)
# print(arr[(arr==6)], type(arr[(arr==6)]))
arr[(arr==6)] = 5
# print(arr)

li3 = np.arange(3)[[False,True,True]]
# print(li3)

"""
批量生成随机数
"""

print(np.random.rand(5, 5))
print(random.random())
print(np.random.randint(3, 10, (3, 4))) # 生成3-10的随机数
print(np.random.choice([2,3,7,1,0],(2,3)))
print(np.random.uniform(10,20,10))


