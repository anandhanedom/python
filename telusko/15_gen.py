def topTen():
    # yield 10
    # yield 9
    # yield 8
    # yield 7
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1  # after return like yield


values = topTen()

print(values.__next__())
print(values.__next__())


for i in values:
    print(i)
