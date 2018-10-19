class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.strs=strs
        out=""
        lst=[]
        try:
            try:
                for i in range(len(self.strs[0])):
                    inc=0
                    for j in range(len(self.strs)-1):
                        if self.strs[j][i]==self.strs[j+1][i]:
                            match=strs[j][i]
                            inc +=1
                        else:
                            break  
                    if inc==len(self.strs)-1:
                        out=out+match
                    else:
                        break
           # for i in range(len(lst)):
               # s=lst[i]
               # out=out+s
            except UnboundLocalError:
                out=out+self.strs[0]
        except IndexError:
            print("this is index error")
            
        return out
                       
                       
                       
                
                       
p1=Solution()
#lst= ["flower","flow","flight"]
lst=["dog","racecar","car"]
print(p1.longestCommonPrefix(lst))
