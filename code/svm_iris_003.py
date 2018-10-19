from sklearn import datasets#to get iris dataset
from sklearn import svm#to fit the svm classifier
import numpy as np


import matplotlib.pyplot as plt
# import iris data to model avm classifier
iris_dataset=datasets.load_iris()


#Modeling Differnt kernel svm classifier using iris sepel features


iris=datasets.load_iris()
X=iris.data[:,:2]
A=iris.data[:,2:]
y=iris.target
c=1.0

#SVC with linear kernel
svc=svm.SVC(kernel='linear',C=c).fit(X,y)#sepel
svc1=svm.SVC(kernel='linear',C=c).fit(A,y)#petel
#linearSVC (linear kernel)
lin_svc=svm.LinearSVC(C=c).fit(X,y)#sepel
lin_svc1=svm.LinearSVC(C=c).fit(A,y)#petel
#SVC with RBF kernel
rbf_svc=svm.SVC(kernel='rbf',gamma=0.7,C=c).fit(X,y)#sepel
rbf_svc1=svm.SVC(kernel='rbf',gamma=0.7,C=c).fit(A,y)#petel
poly_svc=svm.SVC(kernel='poly',degree=3,C=c).fit(X,y)#sepel

poly_svc1=svm.SVC(kernel='poly',degree=3,C=c).fit(A,y)#petel
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
        'SVC with polynomial (degree3) kernel',
        'SVC with linear kernel for petels',
        'linearSVC(linear kernel)  for petels',
        'SVC with RBF kernel for petels',
        'SVC with polynomial kernel for petels ']

for i,clf in enumerate((svc,lin_svc,rbf_svc,poly_svc,svc1,lin_svc1,rbf_svc1,poly_svc1)):
    plt.subplot(4,2,i+1)
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


   # plt.subplot(2,2,i+1)
    plt.subplots_adjust(wspace=0.4,hspace=0.8)
    Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
    
    
    plt.scatter(A[:,0],A[:,1],c=y,cmap=plt.cm.coolwarm)
    plt.xlabel('petel Length')
    plt.ylabel('petel width')
    plt.xlim(xx.min(),xx.max())
    plt.ylim(yy.min(),yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])
plt.show()
