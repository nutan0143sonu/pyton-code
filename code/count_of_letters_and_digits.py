'''
write a program that accepts a sentence and calculate the number of letters
and digits.ex-input-hello world!123
output-letters 10
digits 3
'''
sentence=input("please enter the sentence")
lst=[]
for i in range(len(sentence)):
    if sentence[i].isalpha() or sentence[i].isdigit():
        lst.append(sentence[i])
        #print("lst is :: ",lst)
    else:
        continue
letter=0;digit=0
for i in range(len(lst)):
    try:
        l=int(lst[i])
        digit +=1
        #print("digit",digit)
    except ValueError:
        letter +=1
       # print("letter",letter)
        
print("LETTERS: ",letter)
print("DIGITS: ",digit)
