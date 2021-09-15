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
print(message[0:2])  # [start:stop] - stop is also excluded
print(message[0:8:2])  # [start:stop:stepover]
print(message[1:])  # start from index 1
print(message[-1])  # last index
print(message[::-1])  # string reversal
