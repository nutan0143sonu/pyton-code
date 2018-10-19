#write a program to calculate the sum of first digit and last digit of a given number
def first_last_digit_of_num(num1):
    num=str(num1)
    first_num=num[0]
    last_num=num[-1]
    sum=int(first_num)+int(last_num)
    print("the additon of first digit ",first_num," and last digit",last_num," of an number is : ",sum)
    return None
number=int(input("enter the number"))
first_last_digit_of_num(number)



#write a prgram to accept a string value from user ,delete all vowels from string and display the result
def del_vowels(string):
    i=0
    lst=list(string.split(','))
    while i<len(lst):
        
        if lst[i]=='a' or lst[i]=='e' or lst[i]=='i' or lst[i]=='o' or lst[i]=='u':
            del lst[i]
            print("after deletion of vowels the string is: ",lst)
        i +=1    
               
    return None
string=input("Enter string")
del_vowels(string)
