'''import numpy as np
data=[[2,6,1,3,7],[5,10,4,9,8]]
print(type(data))#<class 'list'> is output
data=np.array(data)
print(type(data))#<class 'numpy.ndarray'> is the output
print(data)#[[ 2  6  1  3  7]
           # [ 5 10  4  9  8]]  is the output
print('-'*30)#----------is the output
print(data.shape)#(2,5) here 2 is no of row and 5 is no of coloumn
print('-'*30)
print(np.zeros((2,3)))#[[0. 0. 0.]
                       #[0. 0. 0.]]
print('-'*30)
print(np.ones((2,3)))#[[1. 1. 1.]
                      #[1. 1. 1.]]
print('-'*30)
array=np.arange(10)#after doing this the list converted in one list as given below
print(array)#[0 1 2 3 4 5 6 7 8 9]
print(array[2:5])#[2 3 4]
array[5:8]=0#it replace value from 5 to 8 into zero
print(array)#[0 1 2 3 4 0 0 0 8 9]
'''

'''
import numpy as np
data=np.array([[5,6,7],[8,9,19]])
print('-'*30)
print(data)#[[ 5  6  7]
           # [ 8  9 19]]
print('-'*30)
print(data+5)#[[10 11 12]
              #[13 14 24]]
print('-'*30)
print(data-3)#[[ 2  3  4]
              #[ 5  6 16]]
print('-'*30)
print(data*data)#[[ 25  36  49]
                 #[ 64  81 361]]
print('-'*30)
#transposing and swapping
data=np.arange(16).reshape(4,4)#[[ 0  1  2  3] it will give matrix of given reshape
                                #[ 4  5  6  7]
                                #[ 8  9 10 11]
                                #[12 13 14 15]]
print(data)
print('-'*30)
#transposing array
print(data.T)#[[ 0  2  4  6  8 10 12 14]
             # [ 1  3  5  7  9 11 13 15]]

print('-'*30)
x=np.random.randn(2,3)
print(x)#[[ 0.29742336 -0.43900303  0.00992125]  here is two row and three coloumn 
         #[ 0.5459569   0.11332597  1.07919604]]
'''
'''
import numpy as np
#random data
data=np.random.randn(3,2)#array([[1.23872308, 0.33769623],
                                #[0.06537867, 0.32935106],
                                #[1.12068716, 0.43488657]])
print('-'*30)
print(data)
print('-'*30)
print(data.mean())#0.5877871306170589
print('-'*30)
print(data.min())
print('-'*30)
print(data.max())
print('-'*30)
'''
'''import numpy as np
#random data
x=np.random.randn(3,2)
x=np.matrix(x)
y=np.random.randn(2,2)
y=np.matrix(y)
print('-'*30)
print(x)
print('-'*30)
print(y)
#multiply the matrix
print('-'*30)
print(x*y)
print('-'*30)
'''
'''import numpy as np
#random data
x=np.random.randn(3,3)
x=np.matrix(x)
y=np.random.randn(3,3)
y=np.matrix(y)
print('-'*30)
print(x)
print('-'*30)
print(y)
#addition of matrix
print('-'*30)
print(x+y)
print('-'*30)
#sub. of matrix
print('-'*30)
print(x-y)
print('-'*30)'''

'''import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np
#import matplotlib.pyplot as plt
objects=('python','c++','java','perl','scala','lisp')#tuple
y_pos=np.arange(len(objects))# now it is numpy.ndarray and it convert it in array
performance=[10,8,7,4,2,1]
plt.bar(y_pos,performance,align='center',alpha=0.9)
plt.xticks(y_pos,objects)
plt.ylabel('usage')
plt.title('programming language usage')
plt.show()'''



'''import matplotlib.pyplot as plt
#data to plot
labels='python','c++','ruby','java'
sizes=[215,130,245,210]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0.1,0,0,0)#explode lst slice
#plot
plt.pie(sizes,explode=explode, labels=labels,colors=colors,
        autopct='%1.5f%%',shadow=True, startangle=190)#%1.1f%%
plt.axis('equal')
plt.show()'''

'''import matplotlib.pyplot as plt
import numpy as np
y=[2,4,6,8,10,12,14,16,18,20]
y2=[10,11,12,13,14,15,16,17,18,19]
x=np.arange(10)
fig=plt.figure()
print("the fig is :: ",fig)
ax=plt.subplot(111)
ax.plot(x,y, label='$y=numbers')
ax.plot(x,y2, label='$y2=other numbers')
plt.title('legend outside')
chartBox=ax.get_position()
print("chartbox",chartBox)
ax.set_position([chartBox.x0,chartBox.y0,chartBox.width*0.6,chartBox.height])
ax.legend(loc='upper center',bbox_to_anchor=(1.45,0.8), shadow=True,ncol=1)
plt.show()'''


import datetime
ob=datetime.datetime.now()
print(type(ob))
print("_"*25)
print(ob)
print(ob.year)
print(ob.month)
print(ob.day)
print(ob.hour)
print(ob.minute)
print(ob.second)
str1=str(ob.hour)+':'+str(ob.minute)+':'+str(ob.second)
print(str1)
print("_")
print("1 week ago  was it:",ob-datetime.timedelta(weeks=1))
print("100 days ago  was it:",ob-datetime.timedelta(days=100))
print("1 week from now:",ob+datetime.timedelta(weeks=1))
print("100 week days from now:",ob+datetime.timedelta(weeks=1))
bday=datetime.datetime(1997,7,2)
print("birthday in....",ob-bday )



















