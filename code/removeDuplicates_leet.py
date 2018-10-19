class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        lst=self.nums
        i=0;j=i+1
        while i<len(lst):
            print("the value of i",i)
            while j<len(lst):
                print("the value of j",j)
                if lst[i]==lst[j]:
                    del lst[j]
                    j=i+1
                    print(lst)
                else:
                    break
                
            i +=1    
        
        return lst
p1=Solution()
lst=[0,0,1,1,1,2,2,3,3,4]
print(p1.removeDuplicates(lst))
