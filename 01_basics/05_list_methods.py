basket = [1, 2, 3, 4, 5]


# addition
basket.append("new-item")
print(basket)

basket.insert(0, 1000)
print(basket)

basket.extend(["grapes", "orange"])
print(basket)


# removal
basket.pop()
basket.pop(0)
print(basket)

basket.remove("new-item")
print(basket)


# lookup
new_basket = [
    "e",
    "a",
    "b",
    "c",
    "d",
]
print(new_basket.index("a"))
# print(new_basket.index("d",0,3)) // stops right before d


print("z" in new_basket)  # exists?
print(new_basket.count("d"))  # how many times?

# new_basket.sort() - same array modification
print(sorted(new_basket))  # returns new array


latest = new_basket.copy()

# new_basket.reverse()

print(latest)


### common list patters ###
print(len(new_basket))