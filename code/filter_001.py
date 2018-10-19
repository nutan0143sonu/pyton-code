def checkEven(x):
    if  x% 2 == 0:
        return True
    else:
        return False
    
lst=[2,1,5,4,9,11,22,33,44,55,66,88]
res=list(filter(checkEven,lst))
print(lst)
print (res)

res1=list(filter(lambda x:x%2==0, lst))
print (res1)


