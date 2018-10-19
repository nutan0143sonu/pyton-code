def table1():
    while True:
        inp=input("please x for exit")
        if inp=='x' or inp=='X':
            break
        else:
            n=int(input("enter the input for table: "))
            i=1
            while i<=10:
                tab=n*i
                print(n,"*",i,"=",tab)
                i +=1
        
    return

table1()
