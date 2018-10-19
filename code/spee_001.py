import os
file_lst=[]
lst=os.listdir("C:\Python\Python36-32\speech recognition project")
for n in lst:
    if(n[len(n)-4:]==".wav"):
        file_lst.append(n)
print(file_lst)
