def say_hello():
    print("Hello world")


def say_name(name="Darth Vader", icon="@"):
    print(f"Helloo {name} {icon}")


# postional arguments - GOOD
say_name("John Doe", "#")

# keyword arguments - BAD
say_name(icon="#", name="Jane Doe")


say_name()


def add(a=0, b=0):
    return a + b


total = add(1, 2)
print(total)

# DOC-STRINGS
def test(a):
    """
    Info: this function tests and prints param a
    """
    print(a)


test(1)
# help(test)
# print(test.__doc__)

# *args and **kwargs - standard names
# Rule: params, *args, default params, **kwargs


def super_function(*args, **kwargs):
    print(args)
    print(kwargs)

    kwargs_sum = 0
    for item in kwargs.values():
        kwargs_sum += item

    return sum(args) + kwargs_sum


print(super_function(1, 2, 3, 4, 5, num1=5, num2=10))
