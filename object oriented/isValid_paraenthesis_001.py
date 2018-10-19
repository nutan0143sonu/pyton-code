class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s=s;lst=[]
        print(len(self.s))
        if len(self.s)%2==0:
            for i in range(len(self.s)):
                print(self.s[i])
                if self.s[i]=="(" or self.s[i]=="[" or self.s[i]=="{":
                    lst.append(self.s[i])
                    print("the list after appending",lst)
                if self.s[i]==")" or self.s[i]=="]" or self.s[i]=="}":
                    if len(lst)!=0:
                        temp=lst.pop()
                        if temp=='(' and self.s[i]==')' :
                            continue
                        elif temp=='[' and self.s[i]==']':
                            continue
                        elif temp=='{' and self.s[i]=='}':
                            continue
                        else:
                             return False
                    else:
                        return False
            if len(lst)==0:
                return True
            else:
                return False
        else:
            return False
        
p1=Solution()
p=input("enter parenthesis")
print(p1.isValid(p))
