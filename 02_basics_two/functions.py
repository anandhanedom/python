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
