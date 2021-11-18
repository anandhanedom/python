def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for_loop([1, 2, 3, 4])
