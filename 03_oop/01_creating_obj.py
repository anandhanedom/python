class PlayerCharacter:
    membership = True  # class object attribute - static

    def __init__(self, name="No Name", age=10):
        self.name = name  # attributes - dynamic
        self.age = age

    def run(self, speed=0):
        print(f"Running at {speed} m/s")

    def shout(self):
        print(f"My name is {self.name}")
        if self.membership:  # if PlayerCharacter.membership also works in this case
            print("I'm a member")
        else:
            print("I'm not a member")

    @classmethod
    def add_things(cls, num1, num2):
        return cls("Jane Doe", num1 + num2)  # instantiation
        # return num1 + num2

    @staticmethod
    def add_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("John Doe", 20)


# help(player1) - blueprint

print(player1.name)
print(player1.age)

player1.run(10)
player1.shout()

print(player1.add_things2(1, 2))  # on instance


print(PlayerCharacter.add_things2(12, 2))

player_2 = PlayerCharacter.add_things(10, 2)  # on class
print(player_2.age)
