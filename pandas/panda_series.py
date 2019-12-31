import numpy as np
import pandas as pd

# 数组和字典的结合体
# 数据和标签组成的


# Series支持数组的特性
# 1、从ndarray创建Series: Series(arr)
# 2、与标量运算
# 3、两个Series运算：sr1 + sr2
# 4、索引：sr[0],sr[[1,2,4]]
# 5、切片：sr[0:2] 依然是视图形式
# 6、通用的函数：np.abs(sr)
# 7、bool值过滤：sr[sr>0]
# 8、统计函数：mean/sum

# Series支持的字典特性
# 1、从字典创建Series: Series(dic)
# 2、in 运算 ：'a' in sr, for x in sr
# 3、键索引：sr['a'] sr[['a', 'b', 'c']]
# 4、键切片：sr['a':'c'] 前包后也包的
# 5、其他的函数：get('a', default=0)

pd1 = pd.Series([3,5,7,9], index=['a','b','c','d'])
# print(pd1)
# print(pd1[0])
# print(pd1['a'])
pd2 = pd.Series({'a':1,'b':2})
# print(pd2)
# print(pd1.values)
# print(pd1.index)
# index 转为 array
# print(pd1.index.values)
# print(np.sqrt(pd1))
# print(pd1.sum())
# print(pd1.mean())
# print(pd1.cumsum())
b = 'e' in pd1
# print(b)
for i in pd1.index:pass
    # print(i)

# 切片是前包后也包的
f = pd1['a':'c']
# print(f)

sr1 = pd.Series([12,23,34],index=['c','a','d'])
sr2 = pd.Series([11,20,10],index=['d','c', 'a'])
# print(sr1 + sr2)
sr3 = pd.Series([11,20,10,14],index=['d','c','a','b'])
# print(sr1.add(sr3, fill_value=0))
sr = sr1 + sr3
# print(sr)

# 处理缺失值
ss = sr.dropna()
# print(ss)

sd = sr.fillna(0)
# print(sd)

# print(sr.isnull())
# print(sr.notnull())
sr[sr.isnull()]=6
# print(sr)



