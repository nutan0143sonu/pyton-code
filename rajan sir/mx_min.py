n=int(input("enter the value of n in list"))
lst=[]
i=0
while i<n:
    element=int(input("enter the element of list"))
    lst.append(element)
    print("now the list after entering input is: ",lst)
    i +=1
max1=max(lst)
min1=min(lst)
print("the maximum value is :",max1)
print("the minimum value in the list:",min1)
