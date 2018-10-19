fo=open("file_handling_001.txt","w")

count=0
while count<5:
    str1=input("enter text:")
    fo.write(str1)
    count=count+1

fo.close()
print("work done")
