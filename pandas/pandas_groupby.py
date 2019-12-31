import pandas as pd
from IPython.display import display

gg = pd.read_csv('groupby_test')
# print(gg)
# print(gg.groupby("name").mean())
for a, b in gg.groupby("name"):pass   # 把数据按组分开
    # display(b)

cs = pd.read_csv("601318.csv",index_col="data", parse_dates=True)
del cs['id']
print(cs)
for a, b in cs.groupby(lambda x:int(cs.loc[x, 'open']//10%10)):  # 按开盘价的每10元分一组
    display(b)

print("*"*20)
"""
分组信息
groups
get_group("a")
for name, group in df.groupby("key")

agg 自定义聚合方式
"""

fg = cs.groupby(lambda x:int(cs.loc[x, 'open']//10%10)).agg(lambda x:x.max()-x.min())
print(fg)

"""
数据拼接

pd.concat([df1,df2,df3], axis=1, keys=,ignore_index='')
df1.append(df2)


数据连接：

pd.merge(df1, df2,on='key',how='inner'/'outer'/left/right)

"""

