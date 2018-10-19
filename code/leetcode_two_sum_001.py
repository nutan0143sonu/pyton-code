class solution:
    def twoSum(self,nums,target):
        len1=len(nums)
        for i in len1:
            sum1=nums[i]+nums[i+1]
            if sum1==target:
                index1=i
                index2=i+1
                break
        x=(index1,index2)
     return x

    lst=[]
    self=int(input("enter the self value"))   
    for j in self:
        val=int(input("enter the value of list"))
        nums=lst.append(val)
    target=int(input("enter the target value"))    
    
        
 
