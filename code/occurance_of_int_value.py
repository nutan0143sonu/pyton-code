#i want to count the occurence of each element in the following list
mylist=[7,9,1,8,4,7,6,9,4,6,9,3,6,9,7]
print(mylist)
temp_dict={1:0,2:0,3:0,4:0}
#s=set(mylist)
lst=[]
for i in range(len(mylist)):
    if mylist[i] not in lst:
        c=mylist.count(mylist[i])
        lst.append(mylist[i])
        print(c)
        if c in temp_dict.keys():
            temp_dict[c] +=1
        else:
            temp_dict[c]=1
    else:
        continue
        
for i,j in temp_dict.items():
    print(i,"=",j)
        
        
        
