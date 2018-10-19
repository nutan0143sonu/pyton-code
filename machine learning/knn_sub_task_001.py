import math

data1=[5.1,3.5,1.4,0.2,0.1,0.9,'Iris-stosa']
data2=[5.4,3.9,1.7,0.4,0.2,0.5,'Iris-stosa']


def euclideanDistance(data1,data2,length):
    distance=0
    for i in range(length):
        distance=distance+((data1[i]-data2[i])**2)
        print("the distance between points or object in length:" ,distance)
    return distance**(1/2)


res=euclideanDistance(data1,data2,2)

print(res)
'''for i in range(length):   #this is another way for finding square root
    distance +=pow((data1[i]-dtat2[i]),2)
    return math.sqrt(distance)
'''
