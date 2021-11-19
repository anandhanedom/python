def get_factorial(number):
    if number == 0:
        return 1
    else:
        return number * get_factorial(number - 1)


five_factorial = get_factorial(5)
print(five_factorial)
