from functools import reduce

my_list = [1, 2, 3, 4]
your_list = [10, 20, 30, 40]

# 1. Map
def multiply_by_two(item):
    return item * 2


print(list(map(multiply_by_two, my_list)))

# 2. Filter
def find_even(item):
    return not item % 2


print(list(filter(find_even, my_list)))

# 3. Zip
print(list(zip(my_list, your_list)))

# 4. Reduce
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
