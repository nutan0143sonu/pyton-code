#linear kernel on two feature of iris data set to classify their class
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets
#import some data to play with
iris=datasets.load_iris()
#print("the iris data is after loading:",iris)
X=iris.data[:, :2]#we only take the first two features,we could
#avoid this ugly slicing by using a two-dim dataset
#print("the value of X:",X)
Y=iris.target
#print("the value of y: ",y)
#we create an instance of svm and fit out data .we do not scale our data since we want to plot the support vector
c=1.0#SVM regularization parameter
svc=svm.SVC(kernel='linear',C=1,gamma=1).fit(X,Y)
#svc=svm.SVC(kernel='rbf',c=1,gamma=1).fit(X,y)
#create a mesh to plot in
x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
h=(x_max/x_min)/100
print("the value of h: ",h)
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
print("the value of xx:",xx)
print("the value of yy:",yy)
plt.subplot(1,1,1)#<matplotlib.axes._subplots.AxesSubplot object at 0x0059B050> is the output
Z=svc.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
plt.contourf(xx,yy,Z,cmap=plt.cm.Paired,alpha=0.8)
plt.scatter(X[:,0],X[:,1],c=Y,cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(),xx.max())
plt.title('svc with linear kernel')
plt.show()


