fo=open(r"C:\Python\Python36-32\file handling\file_handling_001.txt","a")#appending the value

while True:
    str1=input("enter tex:")
    fo.write(str1+'\n')
    choice=input("to exit type x:")
    if choice=='x' or choice=='X':
             break
    else:
             continue
fo.close()
print("work done")             
             
             
             
