def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))

        except StopIteration:
            break


special_for_loop([1, 2, 3, 4])

# range implementation
class MyGen:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first < self.last:
            num = self.first
            self.first += 1
            return num

        raise StopIteration


range_10 = MyGen(5, 10)

for i in range_10:
    print(i)
