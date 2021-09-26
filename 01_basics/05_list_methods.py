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
