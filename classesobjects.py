# A class is a blueprint of an object
# An Object is an instance of a class

class Person:
    #Properties/attributes/vaiables/characteristics
    name = "James"
    age = 23
    gender = "Male"

    # Methods/Function/Behaviour
    def move(self):
        print("person is walking")

farmer = Person()
farmer.move()
print(farmer.gender)
