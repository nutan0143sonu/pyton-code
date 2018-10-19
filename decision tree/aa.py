import numpy as np
from sklearn import tree
clf=tree.DecisionTreeClassifier()

#[height,hair-length,voice-pitch]

import random
datalst=[]
with open('iris.txt') as ob:
    for line in ob:
        str1=line.split(',')
        datalst.append(str1)
#print (datalst)
trng=random.sample(datalst,100)
test=random.sample(datalst,10)
#print(trng)
trng_x=[]
trng_y=[]
test_x=[]
for i in trng:
    trng_x.append(i[:4])
    t=i[-1]
    trng_y.append(t[0:-1])

for i in test:
    test_x.append(i[:4])
#print(trng_x)
#print(trng_y)
print("test:: ",test_x)

#for training set converstion into float
training_x=[]
for i in range(len(trng_x)):
    float1=[];j=0
    while j<4:
        float1.append(float(trng_x[i][j]))
        #print("float1:: ",float1)
        j +=1
    training_x.append(float1)
    #print("training_x:: ",training_x)
        

#for test set conversion into float
testSet_x=[]
for i in range(len(test_x)):
    float1=[];j=0
    while j<4:
        float1.append(float(test_x[i][j]))
        #print("float1:: ",float1)
        j +=1
    testSet_x.append(float1)
    #print("training_x:: ",testSet_x)


trng_data=np.array(training_x)
#print(trng_data)

'''        
X=[[180,15,0],
   [167,42,1],
   [136,35,1],
   [174,15,0],
   [141,128,1]]
Y=["man","woman","woman","man","woman"]
'''
'''
def getAccuracy(test,predict):
    correct=0
    for x in range(len(test)):
        print(test[x][-1],predict[x])
        if test[x][-1]==predict[x]:
            correct +=1
    return (correct/float(len(test)))*100.0
'''
clf=clf.fit(trng_data,trng_y)#it is used for train
print("the clf is:: ",clf)
predict=[]
for i in range(len(testSet_x)):
    prediction=clf.predict([testSet_x[i]])
    print(prediction)
   # predict.append(prediction)
#print(predict)
#accuracy=getAccuracy(test,predict)
