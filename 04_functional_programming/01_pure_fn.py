# 1. Same output
# 2. No side effects

# example
def multiply_by_two(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list


print(multiply_by_two([1, 2, 3]))
