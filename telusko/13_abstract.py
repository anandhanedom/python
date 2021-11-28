from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running...")


class Whiteboard(Computer):  # enforcing WhiteBoard to define process method
    def write(self):
        print("its writing")


class Programmer:
    def work(self, com):
        print("Solving bugs...")
        com.process()


# com = Computer()
com1 = Laptop()
com2 = Whiteboard()
# com1.process()


prog1 = Programmer()

prog1.work(com1)
prog1.work(com2)
