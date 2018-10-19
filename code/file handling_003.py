try:
    num1=int(input("enter the number"))
    num2=int(input("enter the number"))
    res=num1/num2
except Exception as ob:
    print(ob)
else:
    
    print(num1,'/',num2,'=',res)
print("Thanks")    
