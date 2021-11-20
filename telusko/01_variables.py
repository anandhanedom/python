num = 5
name = "john doe"

print(id(num))
print(id(name))

a = 10
b = a


# Address based on the box itself not variable name
print(id(a))
print(id(b))
print(id(10))


a = 9
print(a)
print(id(a))
print(id(b))  # b still references 'box 10'
print(b)


list1 = [1, 2]
list2 = list1
list1.append(0)
print(list1)
print(list2)
