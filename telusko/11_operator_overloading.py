class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3


s1 = Student(58, 69)
s2 = Student(60, 65)


s3 = s1 + s2  # => Student.__add__(s1,s2) - overloading '+ operator'

print(s3.m1)


s4 = s1.__add__(s2)
print(s4.m1)
