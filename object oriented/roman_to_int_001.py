class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s=s
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum1=0;print("the value of sum",sum1);i=0
        try:
            while i<len(self.s):
                if roman[self.s[i]]>=roman[self.s[i+1]]:
                    print(" the value of roman[self.s[i]] is ",roman[self.s[i]]," and the value of roman[self.s[i+1]] " ,roman[self.s[i+1]])
                    sum1=sum1+roman[self.s[i]]
                    i +=1
                    print("the value of sum after addtion of r ",sum1)
                elif roman[self.s[i]]<roman[self.s[i+1]]:
                    if sum1!=0:
                        r=roman[s[i+1]]-roman[s[i]]
                        sum1=sum1+r
                        print("the value of sum is ",sum1)
                        i +=2
                    else:
                        r=r=roman[s[i+1]]-roman[s[i]]
                        sum1=r
                        i +=2
                else:
                    pritn("now end")
                    i +=1
        except IndexError:
          sum1=sum1+roman[self.s[i]]
        
       
        return sum1
while True:
    choice=input("enter your choice for exit enter x")
    if choice!='x' or choice!='X':
        roman=input("enter roman value")
        roman1=roman.upper()
        p1=Solution()
        print(p1.romanToInt(roman1))
   else:
       break








 
