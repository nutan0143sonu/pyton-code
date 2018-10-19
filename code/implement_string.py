class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        self.haystack=heystack
        #print(len(heystack))
        self.needle=needle
       # print(len(needle))
        k=-1;ind=0
        i=0
        while i<len(heystack):
            j=0
            while j<len(needle):
                print("the i is ",i," the j is ",j)
                print("heystack[i]",heystack[i],"needle[j]",needle[j])
                if heystack[i]==needle[j]:
                    if j==0:
                        k=i
                    j +=1
                    i +=1
                    print("the value of k is",k)
                else:
                    k=-1
                    j=0
                    i +=1
                    print("the value of k is",k)
            if j==len(needle):
                break
            
        return int(k)
            
p1=Solution()
heystack="hello"
needle="ll"
print("the return value is ",p1.strStr(heystack,needle))
