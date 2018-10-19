#write a programto accept a string from user and delete all vowels from the string and display the result

string=input("enter the string :: ")
lst=[]
for i in range(len(string)):
    lst.append(string[i])
    #print("the list is :: ",lst)
for i in range(len(lst)):
    if lst[i]=='a' or lst[i]=='e' or lst[i]=='i' or lst[i]=='o' or lst[i]=='u':
        del lst[]
