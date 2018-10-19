#os module interact with your system
#navigating directories

import os
#where are we
#cwd=os.getcwd()
print("1:",os.getcwd())
#go down
os.chdir("rainy_day")
print("2:",os.getcwd())

#go backup
os.chdir(os.pardir)
print("3:",os.getcwd())

os.chdir(os.pardir)
print("4:",os.getcwd())


for file_name in os.listdir("C:\Python\Python36-32\speech recognition project"):
    print(file_name)
