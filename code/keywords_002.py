def printseries(x,y,c):
    start=x
    end=y
    inc=3
    while(start<=end):
        print(start,end=',')
        start +=c
    while(start>=end):
        print(start)
        start -=c
    return None

printseries(10,30,2)

printseries(30,10,3)
