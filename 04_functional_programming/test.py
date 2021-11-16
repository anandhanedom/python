my_list = [2, 3, 4, 5]

# squaring
print(list(map(lambda item: item ** 2, my_list)))

# list sorting by 2 item
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda item: item[1])
print(a)
