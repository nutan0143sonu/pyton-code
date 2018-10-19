import demjson
#encode Encodes the python object into a JSON string representation
#decode Decodes JSON-encoded string into python object
data= [{'a':1,'b':2,'c':3,'d':4,'e':5},
       {'x':11,'y':22}]
print(data,'its data type is',type(data))
print(data[0])
jsonstr1=demjson.encode(data)
print(jsonstr1,'its data type is ',type(jsonstr1))
str2=denjson.decode(jsonstr1)
print(str2)
print(str2,'its data type is',type(str2))
