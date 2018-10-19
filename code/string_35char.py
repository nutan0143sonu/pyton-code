def string1(a,b):
    x=len(a)
    no1=35-x
    no2=no1-len(b)
    print(a,'-'*no2,b)
    return None
str1=input("Enter the first String")
str2=input("Enter the second String")
string1(str1,str2)

def person_info(height1,height2,year1,year2):
   height=height1-height2
   years=year1-year2
   if height>0 and years>0:
       print("Erin's is both Older and Taller then Dale's.")
   
   elif height<0 and years<0:
       print("Dale's older and taller then Erin's")
   else:
       print("There is no name for taller and older")


erins_height=int(input("enter the height of Erin's in cm"))
dales_height=int(input("enter the height of Dale's in cm"))
erins_year=int(input("enter the age of Erin's in years"))
dales_year=int(input("enter the age of Dale's in years"))
person_info(erins_height,dales_height,erins_year,dales_year)
    
