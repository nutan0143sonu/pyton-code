#write a program to accept "n " number from user ,store these number into an array and sort the number of an array  using function

number=[]
n=int(input("enter the n value for an list"))
for i in range(n):
    element=int(input("enter the number for list"))
    number.append(element)
    print("after entering the list is: ",number)
number.sort()
print("After sorting the list, the list is : ",number)
