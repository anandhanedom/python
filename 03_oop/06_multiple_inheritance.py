class User:
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining..")

    def run(self):
        print("Ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hybridorg1 = HybridBorg("Borgie", 50, 100)

hybridorg1.check_arrows()
hybridorg1.attack()
hybridorg1.sign_in()
