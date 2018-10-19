"planet=['Mercury','Venus','Earth',Mars,'Jupiter','Saturn','Neptune','Uranus','Pluto']\
 3.1) write three different ways of removing the last value.pluto from the list of planets. two of these use the method pop\
 3.2) write code to insert 'Asteroid belt' between 'Mars' and 'Jupiter'."
planet=[]
planet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Neptune','Uranus','Pluto']
first=planet.pop()
print("The first method for removing last value is planet.pop()",first," is removed")
planet.append('Pluto')
print('-'*30)
index1=planet.index('Pluto')
del planet[index1]
print("The second method for removing last value is del planet[index]",first," is removed")
planet.append('Pluto')
print('-'*30)
planet.pop(index1)
print("The Third method for removing last value is plantet.pop(index)",first," is removed")
planet.append('Pluto')
print('-'*30)
index2=planet.index('Jupiter')
planet.insert(index2,'Asteroid belt')
print("asteroid belt are inserted between Mars and Jupiter",planet)

