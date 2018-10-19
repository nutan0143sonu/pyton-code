import cal_001

def add(n1,n2):
   temp=n1+n2
   return temp

def sub(n1,n2):
   temp=n1-n2
   return temp


def mul(n1,n2):
   temp=n1*n2
   return temp


def div(n1,n2):
   temp=n1/n2
   return temp


def mod(n1,n2):
   temp=n1%n2
   return temp

def square(n1):
   temp=n1*n1
   return temp
 
def exponential(n1,n2):
    temp=n1**n2
    return temp

def root(n1):
    temp=n1**(1/2)
    return temp



if __name__=='__main__':
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    print (num1 ,'+', num2,'=',add(num1,num2))
    print (num1,'-', num2,'=',sub(num1,num2))
    print (num1,'*', num2,'=',mul(num1,num2))
    print (num1,'/', num2,'=',div(num1,num2))
    print (num1,'%', num2,'=',mod(num1,num2))
    print ('square of',num1,'=',square(num1))
    print (num1,'**', num2,'=',exponential(num1,num2))
    print ('root of ',num1,'=',root(num1))

