def demo():
    print("def is a keyword that is used to help in define a funtion")
    return
def demo1():
    print("def is a keyword that is used to help in define a funtion with return None")
    return None

def add(x,y):
    temp=(x**2 + y**2)**(0.5)
    return temp

def evenodd(x):
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")
    return None    
demo()
demo()
x=demo1()
print(x)
z=add(2,3)
print(z)
evenodd(10)
evenodd(23)
