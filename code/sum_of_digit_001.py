#writea program to calculate the the sum of digit of a given number

sum=0
digit=int(input("enter the digit for calculation"))
str1=len(str(digit))
length=int(str1)
for i in range(length):
    
    modu=digit%10
    quo=digit/10
    q=int(quo)
    digit=q
    sum=sum+modu
print("the sum of digit is :",sum)    
