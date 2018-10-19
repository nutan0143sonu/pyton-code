#Dog clas inherit from wolf class with the same attribute or method ,it override them
class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grrr.....")


class Dog(Wolf):
    def bark(self):
        print("woof")


pet1=Dog("tommy","brown")
pet1.bark()

pet2=Wolf("Jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()#####
#redefine amethod of baseclass in derived class is overrriding
