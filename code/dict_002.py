Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(d1.get(1))
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(d1.get(1))
NameError: name 'd1' is not defined
>>> d1={1:"one",2:"two"}
>>> print(d1.get(1))
one
>>> print(d1.get(2))
two
>>> print(d1.get(3))
None
>>> print(d1.get("one"))
None
>>> print(d1.items())
dict_items([(1, 'one'), (2, 'two')])
>>> print(d1[1]))
SyntaxError: invalid syntax
>>> print(d1.keys())
dict_keys([1, 2])
>>> print(d1.pop(1))
one
>>> print(d1.pop(2))
two
>>> print(d1.pop(2,100))
100
>>> d1
{}
>>> d1={1:"one",2:"two"}
>>> print(d1.popitem())
(2, 'two')
>>> d1
{1: 'one'}
>>> d1={1:"one",2:"two"}
>>> d1
{1: 'one', 2: 'two'}
>>> print(d1.pop(1))
one
>>> print(d1.pop(1,))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(d1.pop(1,))
KeyError: 1
>>> d1={1:"one",2:"two"}
>>> print(d1.popitem())
(2, 'two')
>>> print(d1.popitem())#randomly koi bhi item pop kr dega
(1, 'one')
>>> d1
{}
>>> d1={1:"one",2:"two"}
>>> d1.get(5)
>>> d1
{1: 'one', 2: 'two'}
>>> x=d1.get(5)
>>> x
>>> print(d1.get(2))
two
>>> print(d1)
{1: 'one', 2: 'two'}
>>> a=dict(one=1,two=2,three=3)#this is also used for create dictionary
>>> a
{'one': 1, 'two': 2, 'three': 3}
>>> b={'one':1,'two':2,'three':3}
>>> b
{'one': 1, 'two': 2, 'three': 3}
>>> c=dict(zip(['one','two','three'],[10,20,30]))
>>> c
{'one': 10, 'two': 20, 'three': 30}
>>> c=dict(zip(['one','two','three'],[10,20,30]))#this is also used for create dictionary
>>> c
{'one': 10, 'two': 20, 'three': 30}
>>> print(dict([('two',2),('one',1),('three',3)]))
{'two': 2, 'one': 1, 'three': 3}
>>> print(dict([('two',2),('one',1),('three',3)]))#list of tuple used for
{'two': 2, 'one': 1, 'three': 3}
>>> x=dict([('two',2),('one',1),('three',3)])#list of tuple used for create dictionay
>>> x
{'two': 2, 'one': 1, 'three': 3}
>>> #list of tuple used for create dictionay
>>> e=dict([('two',2),('one',1),('three',3)])#list of tuple used for create dictionay
>>> print(a==b==c==d==e)
False
>>> d
{'two': 2, 'one': 1, 'three': 3}
>>> help('d')
No Python documentation found for 'd'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> d
{'two': 2, 'one': 1, 'three': 3}
>>> f=dict()
>>> f
{}
>>> help(f)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
