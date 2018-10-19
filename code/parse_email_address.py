'''
write a function that takes a string holding an e-email address and returns a lst with two items.
the username,followed by a list of the steps we will need to take to rout the mail.
ex-input---jparker@world.std.com
output---['jparker',['com','std','world']]
'''

def parse_email_address(string):
    lst=[]
    address=string.split("@")
    #print(address)
    lst.append(address[0])
    lst1=[]
    #print(lst)
    address1=address[1].split(".")
    #print("address1",address1)
    address1=address1[::-1]
    #print("address1",address1)
    lst.append(address1)
    #print(lst)
    return lst
    
string=input("Please enter the address")
print("output:: ",parse_email_address(string))
