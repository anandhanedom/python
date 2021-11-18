# Errors : syntax, name error, index error, key error, ......

# def sum(num1, num2):
#     try:
#         return num1 / num2

#     except (TypeError, ZeroDivisionError) as err:
#         print(f"Oops ... {err}")

#     except TypeError as err:
#         print(f"Please enter numbers {err}")

#     finally:
#         print("Finally done!")


# print(sum(2, "1"))

# test..

while True:
    try:
        age = int(input("What is your age? "))
        10 / age
        raise Exception("Hey, cut it out")  # like throw in JS
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Please enter an age greater than 0")
        break
    else:
        print("Thank you!")
        break
    finally:
        print("Finally done!")
    print("can you hear me?")
