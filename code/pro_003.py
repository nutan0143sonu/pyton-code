"'+': addition\
'-':subtraction\
'*':Multiplication\
'\':Division\
'%':Modulus division\
'x':exit"


lst=[]
print("intial list is:",lst)
while True:
    print("+: Addition")
    print("-: Subtraction")
    print("*: Multiplication")
    print("/: Division")
    print("%: Modulus Division")
    print("x: Exit")

    operator=input("enter choice of operator for operation")
   
    if operator=='+':
        
       num1=int(input("enter the first number: "))
       num2=int(input("enter the second number: "))
       temp= num1+num2
       print("num1",'+','num2',"=",temp)
    elif operator=='-':
         num1=int(input("enter the first number: "))
         num2=int(input("enter the second number: "))
         temp= num1-num2
         print("num1",'-','num2',"=",temp)
        
    elif operator=='*':
         num1=int(input("enter the first number: "))
         num2=int(input("enter the second number: "))
         temp= num1*num2
         print("num1",'*','num2',"=",temp)
    elif operator=='-':
         num1=int(input("enter the first number: "))
         num2=int(input("enter the second number: "))
         temp= num1/num2
         print("num1",'/','num2',"=",temp)
    elif operator=='%':
         num1=int(input("enter the first number: "))
         num2=int(input("enter the second number: "))
         temp= num1%num2
         print("num1",'%','num2',"=",temp)
    elif operator=='x' or operator=='X':
        break
    else:
        break
    
print("Thanks")    
