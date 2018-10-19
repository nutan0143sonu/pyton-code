#importing scikit learn with make_blobs
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
#import numpy as np
#creating dataset X containing n_sample
#y containig two classes
X,Y=make_blobs(n_samples=500,centers=3,random_state=0,cluster_std=0.50)
print(X.shape)
print(X)
print(Y.shape)
print(Y)
#plotting scatters
plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap='spring');
plt.show()
