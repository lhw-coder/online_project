"""
1可以把决策树看作是一个if-then规则的集合。
由决策树的根节点到叶子节点就是构建一条规则
中间节点就是条件
数据充足

步骤：
特征选择
决策树生成
决策树剪枝

香农熵
"""

import numpy as np
import pandas as pd

def create_data():
    row_data = {"no surfacing":[1,1,1,0,0],
                "flippers":[1,1,0,1,1],
                "fish":['yes','yes','no','no','no']}
    data_set = pd.DataFrame(row_data)
    return data_set

def calent(data_set):
    n = data_set.shape[0]
    iset = data_set.iloc[:,-1].value_counts()
    p = iset/n
    ent = (-p*np.log2(p)).sum()
    return ent

data_set = create_data()
data = calent(data_set)

# 选择最优的列进行

def bast_split(data_set):
    base_ent = calent(data_set)
    bastGain = 0
    axis = -1
    for i in range(data_set.shape[1]-1):
        levels = data_set.iloc[:,i].values_counts().index
        ents=0
        for j in levels:
            childset = data_set[data_set.iloc[:,i]==j]
            ent = calent(childset)
            ents += (childset.shape[0]/data_set.shape[0]*ent)
        infogain = base_ent - ents
        if (infogain) > bastGain:
            bastGain = infogain
            axis = i
    return axis

def mysplit(data_set, axis,value):
    col = data_set.columns[axis]
    redata_set = data_set.loc[data_set[col]==value,:].drop(col,axis=1)
    return redata_set


