my_list = [2, 3, 4, 5]

# squaring
print(list(map(lambda item: item ** 2, my_list)))

# list sorting by 2 item
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda item: item[1])
print(a)


some_list = ["a", "b", "c", "b", "b", "d", "m", "n", "n"]
duplicates = set([character for character in some_list if some_list.count(character) > 1])
print(duplicates)