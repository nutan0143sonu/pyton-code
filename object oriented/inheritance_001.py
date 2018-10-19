#inheritance is a way to share functionality between classes
class Animal: #superclass
    def __init__(self,name,color):
        self.name=name
        self.color=color
#cat and dog are subclass
class Cat(Animal):#to inherit a class from another class,
    #put superclass name into the parenthesis after the class name
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("woof")

if __name__=="__main__":
     pet1=Dog("tommy","brown")
     pet2=Cat("lucy","white")

     pet1.bark()
     
     pet2.mew()
     print(pet1.name)
     print(pet2.name)
