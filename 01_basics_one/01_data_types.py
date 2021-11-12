# Fundamental data types

# int
# float
# complex
# str
# bool
# list
# tuple
# set
# dict

# type conversion
# str()
# int()
# type()

# int and float
print(type(1 + 2))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(5 // 4)  # gets rounded to integer

# strings
long_string = """ 
wow
wow
wow
"""

print(long_string)


name = "john doe"
age = 55
print(f"hi {name}. you are {age} years old")  # like template strings in js

message = "01234567"
print(message[0:2])  # [start:stop] - stop is omitted
print(message[0:8:2])  # [start:stop:stepover]
print(message[1:])  # start from index 1
print(message[-1])  # last index
print(message[::-1])  # string reversal


# boolean

print(bool(""))
is_cool = False
print(bool("some string"))

# list - arrays
list2 = [1, "a", True, 1.5]


list3 = list2[:]  # make a copy instead of referencing the same array

# dictionary - dictionary keys need to be hashable - no list
dictionary = {"a": [1, 2, 3], "b": "hello", "c": True}
print(dictionary["a"])


# tuple - immutable lists
my_tuple = (1, 2, 3, 4, 5, 6)

# sets
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # only return unique items
