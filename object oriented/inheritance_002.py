#Dog class is inherit from wolf class
class Wolf:
    price=5000
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grrr......")

class Dog(Wolf):
    def bark1(self):
       print("woof")


if __name__=="__main__":
    pet1=Dog("tommy","brown")
    pet1.bark()
    pet1.bark1()
    print(pet1.name,"is of color",pet1.color)
