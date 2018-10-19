Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Python/Python36-32/rajan_sir_power_of.py ============
Enter the value of x4
Enter the value of y2
Enter the value of z3
>>> 
============ RESTART: C:/Python/Python36-32/rajan_sir_power_of.py ============
Enter the value of x4
Enter the value of y3
Enter the value of z2
the x 4  power of y+z 5  is the  1024
>>> 
================= RESTART: C:/Python/Python36-32/dic_001.py =================
<class 'dict'>
{'Name': 'Trng', 'age': 7, 'class': 'First'}
Traceback (most recent call last):
  File "C:/Python/Python36-32/dic_001.py", line 5, in <module>
    print("Keys",dicts.keys())
NameError: name 'dicts' is not defined
>>> 
================= RESTART: C:/Python/Python36-32/dic_001.py =================
<class 'dict'>
{'Name': 'Trng', 'age': 7, 'class': 'First'}
Keys dict_keys(['Name', 'age', 'class'])
Values dict_values(['Trng', 7, 'First'])
Items dict_items([('Name', 'Trng'), ('age', 7), ('class', 'First')])
dict['Name'] Trng
dict['age'] 7
>>> d1={1:"one",2:"two"}
>>> print(d1.values())
dict_values(['one', 'two'])
>>> print(d1.keys())
dict_keys([1, 2])
>>> d1.clear()
>>> print(d1)
{}
>>> d1={1:"one",2:"two"}
>>> d2=d1.copy()
>>> print(id(d1))
99404752
>>> print(id(d2))
99404704
>>> 
