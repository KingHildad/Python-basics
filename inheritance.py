class Animal:
    hasScales = True
    def sound(self):

        print("Animal is speaking")

#Child class/Sub class/Derived class
class Duck(Animal):
    hasWings = True
    def move(self):
        print("Duck is swimming")

class Caterpillar(Duck):
    def move(self):
        print("Caterpillar is slithering")


a = Animal()
d = Duck()

c = Caterpillar()

