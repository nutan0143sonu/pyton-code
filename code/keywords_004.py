num1=int(input("enter a no"))
num2=int(input("enter a no"))
try:
    res=num1/num2
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
    print("Thanks")
