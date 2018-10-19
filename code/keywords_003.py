def printseries(x):
    for i in x:
        #print(x,end=',')now it will print whole list 6 times because list me 6 value hai
        print(i,end=',')
    return None

def prints1(x):
    for i in x:
        print(i[0],end=',')
    return None    

lst1=[[10,20,40],[23,'nutan',50],['java','gupta']]
prints1(lst1)
print('-'*30)
lst=[10,'python',[11,32,34],'java',('mobile',56),20]
printseries(lst)
print('-'*20)
