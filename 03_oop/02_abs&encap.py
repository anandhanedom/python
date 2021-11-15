class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # _ denotes private variables - no true privacy
        self._age = age

    def run(self):
        print("Run")

    def speak(self):
        print(f"My name is {self.name}, and Im not a programmer")


player1 = PlayerCharacter("John", 100)
player1.speak()
