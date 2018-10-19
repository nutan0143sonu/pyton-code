"write a function that returns the middle value among three integer.write code to test with differnt input."
def middle(a,b,c):
    max1=max(a,b,c)
    min1=min(a,b,c)
    print("max value is: ",max1)
    print("man value is: ",min1)
    if a==max1 and b==min1 or b==max1 and a==min1:
        print("the middle value is :",c)
    elif  a==max1 and c==min1 or c==max1 and a==min1:
        print("The middle value is: ",b)
    else:
        print("The middle value is: ",a)
    return None

x=int(input("enter the first integer value"))
y=int(input("enter the second integer value"))
z=int(input("enter the third integer value"))
middle(x,y,z)
