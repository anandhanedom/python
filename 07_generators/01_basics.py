# Without gen ...
def make_list(number):
    result = []
    for i in range(1, number + 1):
        result.append(i)
    return result


my_list = make_list(50)
print(my_list)


def gen_function(number):
    for i in range(number):
        yield i


gen_10 = gen_function(10)

print(next(gen_10))  # 0
print(next(gen_10))  # 1

# because of above nexts : *2,....,*9
for i in gen_10:
    print(f"*{i}")
