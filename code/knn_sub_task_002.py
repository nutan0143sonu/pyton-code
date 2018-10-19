import csv
import random
import math
import operator

fn="C:\Python\Python36-32\iris.txt"
divide=0.70

def loadDataset(filename,split,trainingSet=[],testSet=[]):#ratio 67,33
    with open(filename) as ifile:
        
         lines=csv.reader(ifile)#csv is used to display data in comma seprated module
         dataset=list(lines)
         for x in range(len(dataset)-1):
             
             for y in range(4):
                 
                 dataset[x][y]=float(dataset[x][y])
             if random.random()<split:
                trainingSet.append(dataset[x])
             else:
                 testSet.append(dataset[x])



def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance +=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)    



'''
#this used to run loadDataset
trnglst=[]
testlst=[]
loadDataset(fn,divide,trnglst,testlst)
print("traing list:\n",trnglst)
print("-"*20)
print("test list:\n",testlst) 
'''
