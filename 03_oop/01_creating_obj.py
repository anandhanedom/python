class PlayerCharacter:
    membership = True  # class object attribute - static

    def __init__(self, name, age):
        self.name = name  # attributes - dynamic
        self.age = age

    def run(self, speed=0):
        print(f"Running at {speed} m/s")

    def shout(self):
        print(f"My name is {self.name}")
        if self.membership:  # if PlayerCharacter.membership also works
            print("I'm a member")
        else:
            print("I'm not a member")


player1 = PlayerCharacter("John Doe", 20)


# help(player1) - blueprint

print(player1.name)
print(player1.age)

player1.run(10)
player1.shout()
