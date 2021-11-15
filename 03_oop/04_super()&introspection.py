class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) - OLD
        super().__init__(email)  # NEW way
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 90, "merlin@gmail.com")
print(wizard1.email)
print(dir(wizard1))
