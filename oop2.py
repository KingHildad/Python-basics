class Car:
    def __init__(self, model, color, manufacturer, yof):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yof = yof

    def speed(self):
        print("The manufacturer of ",self.color,"is ",self.model)

car1 = Car("bmw","m12","white",2014)
car1.speed()
car2 = Car("bmw","m12","white",2014)
car2.speed()
car3 = Car("bmw","m12","white",2014)
car3.speed()
car4 = Car("bmw","m12","white",2014)
car4.speed()






