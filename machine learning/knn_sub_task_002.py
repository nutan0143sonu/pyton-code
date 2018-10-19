import csv
import random
import math
import operator

fn="C:\Python\Python36-32\iris.txt"
#divide=0.70

def loadDataset(filename,split,trainingSet=[],testSet=[]):#ratio 67,33
    with open(filename) as ifile:
        
         lines=csv.reader(ifile)#csv is used to display data in comma seprated module
         dataset=list(lines)
         #print("the dataset after split of iris file is ::",dataset)#it provide list of list
         for x in range(len(dataset)-1):
             
             for y in range(4):
                 
                 dataset[x][y]=float(dataset[x][y])
                 #print("after the conversion in float the dataset row is :: ",dataset[x][y])
             if random.random()<split:
                trainingSet.append(dataset[x])
            
             else:
                 testSet.append(dataset[x])



def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance +=pow((instance1[x]-instance2[x]),2)
        return math.sqrt(distance)


def getNeighbour(trainingSet,testInstance,k):
    distances=[]
    length=len(testInstance)-1
   # print("the length of testInstance",length)
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
       # print((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    #print(distances)
    neighbour=[]#it is list of nearest point
    for x in range(k):
        neighbour.append(distances[x][0])
       # print("neighbour",neighbour)
        #print("lengh",len(neighbour))
    return neighbour




def getResponse(neighbours):#it return sorted vote with highest votes
    classVotes={}
    for x in range(len(neighbours)):
        response=neighbours[x][-1]
        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response]=1
        sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
        return sortedVotes[0][0]

def getAccuracy(testSet,prediction):
    correct=0

    for x in range(len(testSet)):
        print(testSet[x][-1],prediction[x])
        if testSet[x][-1]==prediction[x]:
            correct +=1
    return (correct/float(len(testSet)))*100.0








def main():
    
    trainingSet=[]
    testSet=[]
    split=0.60
    loadDataset(fn,split,trainingSet,testSet)
    #print("TrainingSet set:\n",trainingSet)
    print("TrainingSet set:\n" + str(len(trainingSet)))
    print("-"*20)
    print("TestSet set:\n" + str(len(testSet)))
    #print("Test set:\n",testlSett)
    #generate prediction
    pridiction=[]
    k=4
    for x in range(len(testSet)):
        neighbour=getNeighbour(trainingSet,testSet[x],k)
        result=getResponse(neighbour)
        
        pridiction.append(result)
        
        print('>prediction='+str(result)+', actual='+str(testSet[x][-1]))
    print(testSet,"\n",pridiction)
    accuracy=getAccuracy(testSet,pridiction)
    print('Accuracy:'+str(accuracy)+'%')
    return
if __name__=="__main__":
    main()

