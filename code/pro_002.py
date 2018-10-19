#1:add an element to list
#2:pop an element from the list
#3:print element to the list
#4:to exit

list=[]
print("list is :",list)
while True:
    print("1:add an element to list")
    print("2:pop an element from the list")
    print("3:print element to the list")
    print("4:to exit")
    number=int(input("enter the number for operation"))
    if number==1:
        element=input("enter element please")
        list.append(element)
    elif number==2:
        list.pop()
    elif number==3:
        print("now the list is:",list)
    elif number==4:
        break
    else:
        break
print("Thanks")
        
