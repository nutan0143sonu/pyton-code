mainlst=[]
fn="C:\Python\Python36-32\iris.txt"
for i in open(fn,"r"):
    str1=i
    lst=list(str1.split(','))
    mainlist.append(lst)

#print(mainlst)
#11=['2.3','3.5','34.6','python']

def fun1(lst):
    maxlen=len(lst)-1
    i=0
    whlie i<maxlen:
          lst[i]=float(lst[i])
          i +=1
    return lst

