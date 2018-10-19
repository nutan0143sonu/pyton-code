#write a program to know that enter inpur is integer value or float value or string
string=input("enter the input please")
lst=[]
f=0
if '.' in string:
    f +=1
    
try:
    if f==1:
        num=float(string)
        print(num," is the float value")
    elif f==0:
        num=int(string)
        print(num,"is the integer")
    else:
        print(string," is string")
except ValueError:
    
      print(string," is string")
