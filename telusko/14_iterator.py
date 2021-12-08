num = [2, 3, 45]
it = iter(num)
print(next(it))


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = TopTen()

print(values)  # same as print(iter(values))


print(next(values))


for i in values:
    print(i)


# For loop working
my_obj = [1, 2, 3, 4, 5, 6]


def custom_for_loop(iterable):
    iter_obj = iter(my_obj)
    while True:
        try:
            element = next(iter_obj)
            print(element)
        except StopIteration:
            break


custom_for_loop(my_obj)
