def checkEven(x):
    if  x% 2 == 0:
        return True
    else:
        return False

def inc(x):
    temp=x*x+1
    return temp

lst=[2,1,5,4,9]
res=list(map(inc,lst))
print(lst)
print (res)


    
lst=[2,1,5,4,9,11,22,33,44,55,66,88]
res=list(filter(checkEven,lst))
print(lst)
print (res)



