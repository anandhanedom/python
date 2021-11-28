class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # no direct overloading
    def sum(self, a=None, b=None, c=None):
        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(22, 21)
print(s1.sum(2, 4))

# method overriding
class A:
    def show(self):
        print("in A show")


class B(A):
    # pass

    def show(self):
        print("in B show")


a1 = B()
a1.show()
