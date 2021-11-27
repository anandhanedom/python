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
