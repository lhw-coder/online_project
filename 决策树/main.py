from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import graphviz
from IPython.display import Image
import pydotplus

wine = load_wine()
dataframe = pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)

# print(dataframe) # 查看数据
feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类',
                '花青素','颜色强度','色调','od280/od315稀释葡萄酸','普胺酸']

# print(wine.target)
# print(wine.target_names)  # 类别的名字
# print(wine.feature_names) # 属性的名字
Xtrain,Xtest,Ytrsin,Ytest = train_test_split(wine.data,wine.target,test_size=0.3)
# print(Xtrain.shape)       # 训练数据类型
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(Xtrain,Ytrsin)
score = clf.score(Xtest,Ytest)
print(score)

dot_data = tree.export_graphviz(clf,
                                feature_names=feature_name,
                                class_names = ['琴酒','雪莉','贝尔摩德'],
                                filled=True,
                                rounded=True
                                )
graph = graphviz.Source(dot_data)  # 决策树
print(graph)
print(clf.feature_importances_) # 重要的特征
print([*zip(feature_name,clf.feature_importances_)])