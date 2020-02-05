from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
# print(iris)
xtrain, xtest, ytrain, ytest = train_test_split(iris.data,
                                                iris.target,
                                                random_state=42)

clf = GaussianNB()
clf.fit(xtrain,ytrain)

clf.predict(xtrain)

clf.predict_proba(xtest)

a = accuracy_score(ytest,clf.predict(xtest))
print(a)

