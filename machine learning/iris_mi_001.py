import csv
import random
import math
import operator

ob=open("C:\Python\Python36-32\iris.txt","r")#simple file open
lines=csv.reader(ob)
dataset=list(lines)
print(dataset)
#Step1. split the data into training dataset and test the dataset 
'''
with open('C:\Python\Python36-32\iris.txt') as ifile:
    lines=csv.reader(ifile)#csv is used to display data in coma seprated module
    dataset=list(lines)
    print(dataset)
    print('-'*10)
'''
