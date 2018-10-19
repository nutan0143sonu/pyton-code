'''
find the first duplicate value the given list
example- input [1,2,3,3,4,5,6]
output-3
input[1,2,3,4]
ouput- -1
'''
#lst=[1,2,3,4]
lst=[1,2,3,3,4,5,6]
def firstDuplicate(lst):
    i=0;l=-1
    while i<len(lst)-1:
        j=i+1
        while j<len(lst):
            if lst[i]==lst[j]:
                l=lst[i]
            if l!=-1:
                break
            j +=1
        if l!=-1:
            break
        i +=1
    return l
print("output:: ",firstDuplicate(lst))
    
        
