x=int(input("enter four digit number"))

i=4
odd=0
even=0
zero=0
while i>0:
    
    modu=x%10
    quotient=x/10
    q=int(quotient)
    if modu==0:
        zero +=1
        x=q
    elif modu%2==0:
        even +=1
        x=q
    elif modu%2!=0:
        odd +=1
        x=q
        
    else:
        break
    i -=1
print("the no. of zero occur",zero)
print("the no. of Even occur",even)
print("the no. of Odd occur",odd)
