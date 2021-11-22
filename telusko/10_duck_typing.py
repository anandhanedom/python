class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyOwnEditor:
    def execute(self):
        print("Spell check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyOwnEditor()
lap1 = Laptop()


lap1.code(ide)
