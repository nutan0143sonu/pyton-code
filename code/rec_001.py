#write a function that compute the area of rectangle.then,write a second fuction that calls this function\
#three times to compute the sruface area of rectangle solid

def area1(w,h):
    area=w*h
    return area
def surface_area(l):
    w1=int(input("enter the value of first width: "))
    h1=int(input("enter the value of first height: "))
    print("the area of rectangle with width",w1," and the height",h1, "is : ",area1(w1,h1))
    x=2
    surface_area_rectangle1=int(x*(w1*l+h1*l+area1(w1,h1)))
    print("the surface area of rectangle in solid with length",l,", width",w1," and height",h1," is : ",surface_area_rectangle1)

    w2=int(input("enter the value of second width: "))
    h2=int(input("enter the value of second height: "))
    print("the area of rectangle with width",w2," and the height",h2, "is : ",area1(w2,h2))
    surface_area_rectangle2=2*(w2*l+h2*l+h2*w2)
    print("the surface area of rectangle in solid with length",l,", width",w2," and height",h2," is : ",surface_area_rectangle2)


    w3=int(input("enter the value of Third width: "))
    h3=int(input("enter the value of Third height: "))
    print("the area of rectangle with width",w3," and the height",h3, "is : ",area1(w3,h3))
    surface_area_rectangle3=2*(w3*l+h3*l+h3*w3)
    print("the surface area of rectangle in solid with length",l,", width",w3," and height",h3," is : ",surface_area_rectangle3)
    return None
l=int(input("enter the length of the rectangle"))
surface_area(l)
