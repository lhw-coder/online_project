import numpy as np
import math
# 通用函数:对数组中所有的元素进行运算的函数
# 一元(一个数组)：abs->||\sqrt ->开方\exp->指数\log->对数\ceil\floor\rint\trunc\   modf  \isnan\isinf \cos\sin\tan
# 二元（两个数组）：add\substract\multiply\divide\power\mod\  maximum\mininum
arr = np.arange(1,10)
arr1 = np.log(arr)
# print(arr1)
# python的四种取整方式
# 向下取整
x1 = math.floor(3.1)
# print(x1)
# 向上取整
x2 = math.ceil(3.1)
# print(x2)
# 四舍五入
x3 = round(3.6)
# print(x3)
# 向0取整
x4 = int(3.9)
# print(x4)
# python的整除是向下取整
x5 = 1 / 2
x6 = -1 // 2
# print(x5)
# print(x6)

# numpy的四种批量的取整方式
# nan not a number --> 0/0 tan90 -1的开方
a = float('3.6')
c = float('nan')
# print(a)
# print(c)
if c != a:
    print('yes')
else:
    print('no')

d = np.sqrt(np.arange(-5,5))
f = d[~np.isnan(d)]
# print(f)

# inf 无穷大 ∞
s = float("inf")
# print(s)
w = np.array([1,-1,0])/0
# print(w)
# [ inf -inf  nan]

# numpy统计方法
# sum\mean\std(标准差)\var(方差)\min\max
# np.std()

# np.random子包，批量生成随机数组
# rand\randint\choice\shuffle\uniform



