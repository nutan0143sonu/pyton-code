#os module interact with your operating system
#create folder ,remove folder ,move folder,change the working directory

import os
curDir=os.getcwd()
print(curDir)#get current working directory
#os.mkdir(r'shivam')#make a new directory
#os.rename(r'shivam',r'trngday3')#change the name of ,or rename,a directory
os.rmdir(r'trngday3')#remove a directory
