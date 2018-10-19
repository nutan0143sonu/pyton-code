#write a function that takes a list of nubers as an input and return combination of all
#numbers whoes sum is more than 10
def list_of_sum(lst):
    i=0
    
    while i<len(lst):
        j=i+1
        while j<len(lst):
            sum1=lst[i]+lst[j]
           
            new=[]
            
            if sum1>10:
                
                new.append(lst[i])
                new.append(lst[j])
                print("the new sub list is:",new)   
            j +=1
        i +=1    
            
        
            
lst=[1,4,9,5,3,9]
tar=10
list_of_sum(lst)
               
