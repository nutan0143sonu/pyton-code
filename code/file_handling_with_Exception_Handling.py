try:
    fh=open(r"C:\Python\Python36-32\file handling\sample_001.txt","r")#w
    fh.write("This my test file for exception")
    z=5/0
except IOError as ob:
    print("Error: can\'t find file or read ")
    print(ob)
except Exception as ob:
    print(ob)
else:
    print("Weritten content in the file is sucessful")
finally:
    fh.close()
