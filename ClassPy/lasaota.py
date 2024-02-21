class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

cat1 = Animal("Sally", 10)
print(cat1.__str__())
del cat1.name
print(cat1.name)
