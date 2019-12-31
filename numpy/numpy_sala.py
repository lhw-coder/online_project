import numpy as np
import random
# 底层需要C语言的库，和底层芯片inter向量运算的加速功能有关
# 主要就是一个ndarray对象 是一个多维数组， 主要做科学计算
li = [random.uniform(100, 200) for _ in range(10000)]
num1 = np.array(li)
# print(li)
num2 = num1 * 6
# print(num2)
# 计算价格*数量
price = [random.uniform(10, 20) for _ in range(100)]
num = [random.uniform(1, 10) for _ in range(100)]
sum = sum(map(lambda x:x[0]*x[1], zip(price, num)))
# print(sum)
arr_price = np.array(price)
arr_num = np.array(num)
sum_arr = (arr_price*arr_num).sum()
# print(sum_arr)
# 加减乘除都可以批量运算
arr0 = np.array([1,2,3,2**32-1])
arr1 = np.array([1,2,3,2**32-1])+1
# print(arr0)
# print(arr1)
# print(arr1.dtype)
# 转换数据类型
arr2 = np.array([1.,2.,3.]).astype('int')
# print(arr2)
np.arange(0,100,0.5)

li = [random.randint(0, 10) for _ in range(20)]
# print(li)
li1 = list(filter(lambda x:x>5 and x%2==0,li))
# print(li1)
arr_li = np.array(li)
arr_li1 = arr_li[arr_li>5]
# print(arr_li)
# bool索引
li3 = np.arange(3)[[False,True,True]]
# print(li3)


# and & 逻辑与运算符和按位与运算符
# and 在python的语法里是关键字 &是运算符是运算符
# 规定关键字不能重新定义，而运算符可以被重新定义。运算符重载
# 例如__add__,__eq__都是重新定义加和等于
arr = np.arange(10).reshape((2,5))
# print(arr)
# 求两个矩阵的交并补集
交集 = arr[(arr>5) & (arr%2==0)]
# print(交集)
并集 = arr[(arr>5) | (arr%2==0)]
# print(并集)
补集 = arr[~(arr>5)]
# print(补集)
# 花式索引
ll = [random.randint(0, 10) for _ in range(20)]
arr_ll = np.array(ll)
ll1 = arr_ll[[1,3,4,5]]
# print(ll1)


la = np.arange(60).reshape((2,3,10))
# print(la)
# 找到该矩阵的某一位置上的数:，的两边都是花式索引时就可以用。
print(la[[0,1],[1,1],[5,6]])

ls = np.arange(15).reshape((3,5))
print(ls)
print(ls[:,[0,1,3]])

print(ls[ls[:,0]%2==0,-2:])




