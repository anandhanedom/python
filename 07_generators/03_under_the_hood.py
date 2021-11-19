def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for_loop([1, 2, 3, 4])

# range implementation


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


range_10 = MyGen(0, 10)

for i in range_10:
    print(i)
