from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")


t1 = Hello()
t2 = Hi()


t1.start()
t2.start()
