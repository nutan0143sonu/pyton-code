from array import *
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        array1=self.nums
        array2=('i',[])
        try:
            i=0
            while i<int(len(array1))-1:
                j=i+1
                while j<int(len(array1)):
                    if array1[i]==array1[j]:
                        array1.remove(array1[j])
                        if array1[i] not in array2:
                            array2.insert(i,array1[i])
                        else:
                            continue
                        j +=1
                    else:
                        break
                i +=1
            
        except TypeError:
            print("type error")
        return array1
p1=Solution()
a=('i',[1,1,2])
print(p1.removeDuplicates(a))
    
