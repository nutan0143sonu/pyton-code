import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets#to get iris dataset
from sklearn import svm#to fit the svm classifier

#iris data
#iris_dataset=datasets.load_iris()

def estimate_coef(x,y):
    #number of observations/points
    n=np.size(x)
    #mean of x and y vector
    m_x,m_y=np.mean(x),np.mean(y)
    #claculating cross deviation and deviation about x
    ss_xy=np.sum(y*x-n*m_y*m_x)
    ss_xx=np.sum(x*x-n*m_x*m_x)
    #calcultaing regression coefficient
    b_1=ss_xy/ss_xx
    b_0=m_y-b_1*m_x
    return(b_0,b_1)

def plot_regression_line(x,y,b):
    #plotting the actual points as scatter plot
    plt.scatter(x,y,color="m" ,marker="o",s=30)
    #predicted response vector
    y_pred=b[0]+b[1]*x
    #plotting the regression line
    plt.plot(x,y_pred,color="g")

    #putting labeles
    plt.xlabel('X')
    plt.ylabel('Y')
    #function to show plot
    plt.show()
'''
#this is for iris data
def main():
    iris=datasets.load_iris()
    X=iris.data[:,0] #sepel 0 coloumn
    #Y=iris.data[:,1]# sepel 1 coloum
    Y=iris.data[:,2]
    #observation
    x=np.array(X)
    y=np.array(Y)

    #estimation coefficient
    b=estimate_coef(x,y)
    print("Estimation coefficient:\nb_0={}".format(b[0],b[1]))

    #plotting regression line
    plot_regression_line(x,y,b)
'''
#this is the sir program

def main():
    
    #observation
   # x=np.array([0,1,2,3,4,5,6,7,8,9])
    #y=np.array([1,3,2,5,7,8,8,9,10,12])

    x=np.array([0,1,9,3,4,25,6,7,30,9])
    y=np.array([1,3,2,5,7,8,8,55,10,12])


    #estimation coefficient
    b=estimate_coef(x,y)
    print("Estimation coefficient:\nb_0={}".format(b[0],b[1]))

    #plotting regression line
    plot_regression_line(x,y,b)
main()
