class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop("lenovo", "ryzen 7", 16)

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("John Doe", 12)
s2 = Student("Jane Doe", 21)


lap1 = s1.lap
lap2 = s2.lap

print(lap1)
print(lap2)

print(id(lap1))
print(id(lap2))


lap10 = s1.Laptop("lenovo", "ryzen 7", 16)
lap11 = s1.Laptop("dell", "ryzen 5", 8)

print(lap10.brand)
print(lap11.ram)

lap1.show()
lap10.show()
