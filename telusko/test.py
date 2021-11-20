# recursion
def get_factorial(number):
    if number == 0:
        return 1
    else:
        return number * get_factorial(number - 1)


five_factorial = get_factorial(5)
print(five_factorial)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        return True if self.age == other.age else False


s1 = Person("Genghis", 101)
s2 = Person("Ceasar", 75)


print(s1.compare_age(s2))

# decorators
def smart_divider(func):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        func(b, a)

    return wrapper


@smart_divider
def div(a, b):
    print(a / b)


div(2, 4)
print("**")
div(4, 2)
