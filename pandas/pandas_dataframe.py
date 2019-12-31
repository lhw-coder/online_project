"""
最常用的数据结构
是一种表格型的数据结构
"""

import pandas as pd

# print(type(pd.DataFrame({"one":[1,2,3,4],"two":[4,3,2,1]}, index=list("abcd"))))

# 最常操作的文件.csv文件 文本文件
df = pd.read_csv("601318.csv") # 读文件
# df.to_csv() # 写文件
real_df = df.loc[:,"data":"low"]
# print(real_df)
# print(type(real_df))
#
# print(real_df.values) # 数据体
# print(type(real_df.values))
#
# print(real_df.dtypes) # 数据体的数据类型
#
# print(real_df.index) # dataframe的行标签
# print(real_df.columns) # dataframe的列标签
# print(real_df.T) # 转置
#
# print(real_df.describe())  # 统计数据 观测数据

"""
切片和索引
"""
# print(real_df['open'][1]) # 先取列后取行
# print(real_df.loc[1,'open']) # 标签 先行后列
# print(real_df.iloc[1,1])     # 下标 先行后列
# print(df[df['open']>21])

# print(real_df.mean())
# print(real_df.sum())
# print(real_df.sort_values("data")) # 排序
# print(real_df.sort_values("open",ascending=False)) # 降序排

r_df = real_df.loc[:,"open":]
# print(r_df)

print(r_df.apply(lambda x:x.max()-x.min()))  # 作用到每一列上的函数，对每一列（series）
print(r_df.apply(lambda x:(x["open"]+x["close"])/2,axis=1)) # 开盘价和收盘价平均
print(r_df.apply(lambda x:pd.Series([x.max(),x.min()],index=["max","min"])))

print(r_df.applymap(lambda x:x+2))  # 作用到每个元素上面

