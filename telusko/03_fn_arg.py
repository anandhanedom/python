# not pass by value, somewhat pass by reference
# a,x (before x=8) referes to the same memory space


def update(x):
    print(f"Id of x: {id(x)}")
    x = 8  # address changes here
    print(f"Inside function: {x}")


# update(10)

a = 10
print(f"Id of a: {id(a)}")
update(a)
print(f"Outside function: {a}")


def sum(a, b):
    c = a + b
    return c


# def sum1(a, *b):
#     c = a
#     for i in b:
#         c += i
#     return c


# def sum2(*b):
#     c = 0
#     for i in b:
#         c += i

#     return c


def person(name, **kwargs):
    print(name)
    print(kwargs)

    for i, j in kwargs.items():
        print(i, j)


person("John", age=28, city="Delhi", mob=9876543)
