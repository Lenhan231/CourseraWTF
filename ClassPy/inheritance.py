class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)  # Call the parent class constructor
        self.age = age


x = Person("John", "Doe")
x.printname()

x = Student("Mike", "Olsen", 13)
print(x.age)