def power_of(x,y,z):
    a=y+z
    power1=x**a
    print("the x",x," power of y+z",a," is the ",power1)
    return power1

x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
z=int(input("Enter the value of z"))
power_of(x,y,z)
