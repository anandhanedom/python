from time import time


def performance(function):
    def wrapper_function(*args, **kwargs):
        t1 = time()
        function(*args, **kwargs)
        t2 = time()
        print(f"Function took: {t2-t1} s")

    return wrapper_function


@performance
def long_time_without_list():
    for i in range(1000000):
        i * 5


@performance
def long_time_with_list():
    for i in list(range(1000000)):
        i * 5


long_time_with_list()
long_time_without_list()
