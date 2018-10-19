#write a program how many element to add in list by user and that much element in list.

lst=[]
count=0
print("list is :",lst)
while True:
    
    element=input("enter an element to add an element to list:")
    lst.append(element)
    print("list is :",lst)
    choice=input("To add anoter element pass 'Y' :")
    if choice=='Y' or choice=='y':
        continue
    else:
        break
print("Thanks")    
