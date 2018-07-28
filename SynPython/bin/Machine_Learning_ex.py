from sklearn.datasets import load_iris
iris=load_iris()
print(iris.data)
print(iris.feature_names)
print(iris.target)#[0,1,2]
print(iris.target_names)#[setosa, versicolor, virginica
X=iris.data#[[][]]
y=iris.target#[0,1,2]

from sklearn.neighbors import KNeighborsClassifier as k #algorithm

knn1=k(n_neighbors=1)#Out of 150, take nearest 1 value and give.. KNN will be the blank module so train it with you data using fit function
knn1.fit(X,y)# fit will train the module
d1=[[3,5,4,2]]#you have given d1 data and want knn to predict which category it belongs
r1=knn1.predict(d1)
print('r1 =', r1)#verginica#2 will be the result
if r1==0:
    print('Setosa')
elif r1==1:
    print('Versicolor')
else:
    print('Virginica')

d2=[[3,5,4,2],[2,3,4,5]]
r2=knn1.predict(d2)
print('r2 = ', r2)

from sklearn.neighbors import KNeighborsClassifier as k1 #algorith
knn2=k1(n_neighbors=5)
knn2.fit(X,y)
d3=[[3,5,4,2]]#you have given d1 data and want knn to predict which category it belongs
r3=knn2.predict(d3)
print('r3 =', r3)#verginica#2 will be the result
if r3==0:
    print('Setosa')
elif r3==1:
    print('Versicolor')
else:
    print('Virginica')

d4=[[3,5,4,2],[2,3,4,5]]
r4=knn2.predict(d4)
print('r4 = ', r4)

from sklearn.linear_model import LogisticRegression#second alogorithm will predict only 1 best result
LR=LogisticRegression()
LR.fit(X,y)
r5=LR.predict(d1)
print('r5 =',r5)

#evaluation of which algorith to be used

from sklearn.metrics import accuracy_score
#send your full data and see if it is producing expected target based on your target data available for existing data and check its acuracy

r6=knn1.predict(X)#neighbor=1
r7=knn2.predict(X)#neighbor=5
r8=LR.predict(X)#LR

acc1=accuracy_score(r6,y)
acc2=accuracy_score(r7,y)
acc3=accuracy_score(r8,y)

print('acc1 =',acc1)#1.0 means 100%
print('acc2 =',acc2)#0.96666666 means 96.66%
print('acc3 =',acc3)#0.96 means 96%

#second way of comparison is through sampling..for eg train 60% data and predict values for 40% and see if it is predicting the expected target..this way, we can evaluate if this alogorithm can be used
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.4)
print('X_train =', X_train)
print('X_test =', X_test)
print('y_train =', y_train)
print('y_test =', y_test)

knn3=k1(n_neighbors=1)
knn4=k1(n_neighbors=5)
LR2=LogisticRegression()
knn3.fit(X_train,y_train)
knn4.fit(X_train,y_train)
LR2.fit(X_train,y_train)

r9=knn3.predict(X_test)
r10=knn4.predict(X_test)
r11=LR2.predict(X_test)

acc4=accuracy_score(r9, y_test)
acc5=accuracy_score(r10, y_test)
acc6=accuracy_score(r11, y_test)

print('acc4 =',acc4)#0.96666666 means 96.66%
print('acc5 =',acc5)#0.96666666 means 96.66%
print('acc6 =',acc6)#1.0 means 100%

#neighbors value can be maximum your row number ..for ef..if your rows are 150, neighbor value can be 150

scores=[]
for i in range(1,25):
    knn=k1(n_neighbors=i)
    knn.fit(X_train, y_train)
    r=knn.predict(X_test)
    s=accuracy_score(r, y_test)
    scores.append(s)
import matplotlib.pyplot as plt
g=plt.plot(range(1,25), scores)
plt.show()
