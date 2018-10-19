import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model,metrics
#load the bostson datasets
boston=datasets.load_boston(return_X_y=False)
#defining feature matrics(X) and response vector(y)
X=boston.data
y=boston.target

#splitting X and y training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=1)

#create linear regression objectt
reg=linear_model.LinearRegression()

#train the model using the training sets
reg.fit(X_train,y_train)

#regression coefficient
print("coefficents: \n",reg.coef_)

#variance score: 1 means perfect prediction
print("Varience score: {}".format(reg.score(X_test,y_test)))

#plot for residual error

##setting plot style
#plt.style.use('fivethirtyeigth')

##plotting residual error in  training center
plt.scatter(reg.predict(X_train),reg.predict(X_train)-y_train,color="green",s=10,label='Train data')

##plotting residual error  in test data
plt.scatter(reg.predict(X_test),reg.predict(X_test)-y_test,color="blue",s=10,label='Test data')

#plotting line for zero residual error
plt.hlines(y=0,xmin=0,xmax=50,linewidth=2)

#plotting legend
plt.legend(loc='upper right')

##plot title
plt.title("Residual Error")

##function to show plot
plt.show()
