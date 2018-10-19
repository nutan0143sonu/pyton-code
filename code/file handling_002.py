num1=int(input("enter the first number"))
num2=int(input("enter the second number"))


try:
    res=num1/num2  #Exception with num2=none value may be
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)

print("Thanks")    
