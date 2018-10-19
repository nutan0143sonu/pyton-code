import numpy as np
data=np.array([[5,6,7],[8,9,19]])
print('-'*30)
print(data)
print('-'*30)
print(data+5)
print('-'*30)
print(data-3)
print('-'*30)
print(data*data)
print('-'*30)

#Transposing and swapping axis

data=np.arange(16).reshape(4,4)
print(data)
print('-'*30)

#Transposing array
print(data.T)
print('-'*30)
x=np.random.randn(2,3)
print(x)
