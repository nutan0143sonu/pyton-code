class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        self.nums=nums
        self.val=val
        print(self.nums)
        i=0
        while i<len(self.nums):
            print("length of nums",len(self.nums))
            print("the val of i is ",i)
            if self.nums[i]==self.val:
                print("the value of self.nums",self.nums[i])
                del self.nums[i]
                if len(self.nums)!=0:
                   i ==i
                   print("again the value of i is ",i)
                print(self.nums)
                
            else:
                i +=1
        return self.nums

p1=Solution()
lst=[3,3]

val=int(input("enter the val"))
print(p1.removeElement(lst,val))
