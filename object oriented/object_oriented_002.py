#Classes are created using the keyword class and an indentation block,
#which contain class method

class Cat:
    price=400 # calss attribute,created by assiging variable within
    #the body
     
    def __init__(self,name,color):#instance attribute
        self.color=color
        self.name=name
    def bark(self):#all method must have self as their first parameter
        print("woof")
        print(self.name,"has",self.price,"price and its color is",self.color)
if __name__=="__main__":
    pet1=Cat("Tommy","brown")
    pet2=Cat("Jonty","White")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)


    
    print(Cat.price)
    Cat("abc","blue").bark()
