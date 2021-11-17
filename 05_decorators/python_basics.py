# Functions are first class citizens in python


def hello():
    print("Hellooo")


greet = hello

del hello

print(greet())  # works since greet still references the memory location


# Higher order function - accepts or returns a function
def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func
