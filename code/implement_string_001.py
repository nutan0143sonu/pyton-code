class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            self.haystack=heystack
            self.needle=needle
            k=-1
            if needle in heystack:
                return heystack.index(needle)
            else:
                return k
        except NameError:
            print("name error")
    
                    
p1=Solution()
heystack="hello"
needle="ll"
print(p1.strStr(heystack,needle))
