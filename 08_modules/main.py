import utility  # cached in pycache

# if import shopping.shopping_cart  # shopping = package, shopping_cart=module

# import shopping.more_shopping.shopping_cart

from shopping.more_shopping.shopping_cart import buy

print(utility)
utility.divide(1, 2)

# print(shopping.more_shopping.shopping_cart.buy("apple"))
print(buy("apple"))
