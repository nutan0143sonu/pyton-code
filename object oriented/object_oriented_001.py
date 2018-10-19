#Classes are created using the keyword class and an indentation block,
#which contain class method

class Cat:

    def __init__(self,color,legs):#instance attribute
        self.color=color
        self.legs=legs
if __name__=="__main__":
    pet1=Cat("ginger",4)
    print(pet1.legs)
    print(pet1.color)


    pet2=Cat("brown",3)
    print(pet2.color)
    print(pet2.legs)
