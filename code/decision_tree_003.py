import re
X=open(r"C:\Python\Python36-32\trainingSetX.txt","r")
Y=open(r"C:\Python\Python36-32\trainingSetY.txt","r")
from sklearn import tree
import csv
a=re.sub('[','',X)
print("a",a)
b=re.sub(']','',a)
print("b",b)
lines=csv.reader(b)
dataset=list(lines)
print(dataset)
clf=tree.DecisionTreeClassifier()
'''
#[height,hair-length,voice-pitch]
X=[[180,15,0],
   [167,42,1],
   [136,35,1],
   [174,15,0],
   [141,128,1]]
Y=["man","woman","woman","man","woman"]

clf=clf.fit(X,Y)#it is used for train
prediction=clf.predict([137,17,1])
print(prediction)
'''
X.close()
Y.close()
