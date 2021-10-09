# dictionary methods

user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

# print(user["name"]) - key error


print(user.get("age"))  # none
print(user.get("age", 55))  # use 55 if no age


user2 = dict(name="john doe")


print("basket" in user)
print(list(user.keys()))
print(list(user.items()))

print(user.pop("age"))
print(user.popitem())
print(user.update({"age": 55}))
