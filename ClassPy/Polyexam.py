class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def traveling(self):
        print("move")

class car(vehicle):
    pass

class boat(vehicle):
    def traveling(self):
        print("sail")

b1 = boat("lkasdjf", 'laskdjhf ')
b1.traveling()