def inc(x):
    temp=x*x+1
    return temp

lst=[2,1,5,4,9]
res=list(map(inc,lst))
print(lst)
print (res)

res1=list(map(lambda x:x*x+1, lst))
print (res1)
