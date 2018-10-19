fo=open(r"C:\Python\Python36-32\file handling\file_handling_002.txt","wt")

str1=input("enter tex:")
x=fo.write(str1)
fo.write('we are using file handling')
fo.write(str1)
fo.close()
print("work done")
