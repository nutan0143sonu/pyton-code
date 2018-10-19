#the python code for the decision tree
#Imorting The Required package
import numpy as np
import csv
import random
#import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#function for iris dataset
fn="C:\Python\Python36-32\iris.txt"
split=0.60
def loadDataset(filename,split,trainingSetX=[],trainingSetY=[],testSetX=[],testSetY=[]):#ratio 67,33
    with open(filename) as ifile:
        
         lines=csv.reader(ifile)#csv is used to display data in comma seprated module
         dataset=list(lines)
         #print("the dataset after split of iris file is ::",dataset)#it provide list of list
         for x in range(len(dataset)-1):
             
             for y in range(4):
                 
                 dataset[x][y]=float(dataset[x][y])
                 #print("after the conversion in float the dataset row is :: ",dataset[x][y])
             if random.random()<split:
                trainingSetX.append(dataset[x][:4])
                trainingSetY.append(dataset[x][4])
            
             else:

                 testSetX.append(dataset[x][:4])
                 testSetY.append(dataset[x][4])


def main():
    fo=open(r"C:\Python\Python36-32\trainingSetX.txt","wt")
    fo1=open(r"C:\Python\Python36-32\trainingSetY.txt","wt")
    clf=tree.DecisionTreeClassifier()
    trainingSetX=[]
    trainingSetY=[]
    testSetX=[]
    testSetY=[]
    split=0.70
    loadDataset(fn,split,trainingSetX,trainingSetY,testSetX,testSetY)
    print("TrainingSetX set:\n" + str(len(trainingSetX)))
    print("TrainingSetY set:\n" + str(len(trainingSetY)))
    print("trainingSetX",trainingSetX)
    fo.write(str(trainingSetX))
    fo.close()
    fo1.write(str(trainingSetY))
    fo1.close()
    #print("-"*20)
    #print("trainingSetY",trainingSetY)
    #print("-"*20)
    print("TestSetX set:\n" + str(len(testSetX)))
    #print("-"*20)
    #print("TestSetY set:\n" + str(len(testSetY)))
    #print("testsetX",testSetX)
    #print("_"*30)
    #print("testsetY",testSetY)
    x=trainingSetX
    y=trainingSetY
    print(type(x))
    clf=clf.fit(x,y)
    prediction=clf.predict(testSetX)
    print("The prediction is",prediction)
        
if __name__=="__main__":
    main()


