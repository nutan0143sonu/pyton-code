from sklearn import datasets#to get iris dataset
from sklearn import svm#to fit the svm classifier
import numpy as np

import matplotlib.pyplot as plt
# import iris data to model avm classifier
iris_dataset=datasets.load_iris()
print("iris dataset description :: ",iris_dataset['DESCR'])
#let's get iris feature and the target classes
print("iris feature data :: ",iris_dataset['data'])
print("iris target:: ",iris_dataset['target'])

#visulizing the relationship between sepal and target classes
def visualize_sepal_data():
    iris=datasets.load_iris()
    X=iris.data[:,:2]#we only take the first two fewature
    y=iris.target
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.title('sepal width and length')
    plt.show()
#visualize_sepal_data()   


def visualize_petal_data():
    iris=datasets.load_iris()
    X=iris.data[:,2:]#we only take the first two fewature
    y=iris.target
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.title('petal width and length')
    plt.show()
#visualize_petal_data()
#Modeling Differnt kernel svm classifier using iris sepel features

iris=datasets.load_iris()
X=iris.data[:,:2]
y=iris.target
c=1.0

#SVC with linear kernel
svc=svm.SVC(kernel='linear',C=c).fit(X,y)#here C is used for pentration mean high pentration more correct output and small pentration mean not more accurate output
#linearSVC (linear kernel)
lin_svc=svm.LinearSVC(C=c).fit(X,y)
#SVC with RBF kernel
rbf_svc=svm.SVC(kernel='rbf',gamma=0.7,C=c).fit(X,y)
poly_svc=svm.SVC(kernel='poly',degree=3,C=c).fit(X,y)

#visiualizing the modeled svm classifier with iris sepal feature
h=.02#step size in the mesh

#create a mesh to plot in
x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

#title for the plots
titles=['SVC with linear kernel',
        'linearSVC(linear kernel)',
        'SVC with RBF kernel',
        'SVC with polynomial (degree3) kernel']

for i,clf in enumerate((svc,lin_svc,rbf_svc,poly_svc)):
    plt.subplot(2,2,i+1)
    plt.subplots_adjust(wspace=0.4,hspace=0.4)
    Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    #put the result into color plot
    Z=Z.reshape(xx.shape)
    plt.contourf(xx,yy,Z,cmap=plt.cm.coolwarm,alpha=0.8)
    #plot also the training points
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel('sepel Length')
    plt.ylabel('sepel width')
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

#plt.show()    

# this is for petel
iris=datasets.load_iris()
X=iris.data[:,2:]
y=iris.target
c=1.0

#SVC with linear kernel
svc=svm.SVC(kernel='linear',C=c).fit(X,y)
#linearSVC (linear kernel)
lin_svc=svm.LinearSVC(C=c).fit(X,y)
#SVC with RBF kernel
rbf_svc=svm.SVC(kernel='rbf',gamma=0.7,C=c).fit(X,y)
poly_svc=svm.SVC(kernel='poly',degree=3,C=c).fit(X,y)

#visiualizing the modeled svm classifier with iris sepal feature
h=.02#step size in the mesh

#create a mesh to plot in
x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

#title for the plots
titles=['SVC with linear kernel',
        'linearSVC(linear kernel)',
        'SVC with RBF kernel',
        'SVC with polynomial (degree3) kernel']

for i,clf in enumerate((svc,lin_svc,rbf_svc,poly_svc)):
    plt.subplot(2,2,i+1)
    plt.subplots_adjust(wspace=0.4,hspace=0.4)
    Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    #put the result into color plot
    Z=Z.reshape(xx.shape)
    plt.contourf(xx,yy,Z,cmap=plt.cm.coolwarm,alpha=0.8)
    #plot also the training points
    plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel('petel Length')
    plt.ylabel('petel width')
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()    


