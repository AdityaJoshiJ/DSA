class hostel:
    def __init__(self):
        self.rent = int(input())
        self.ram = int(input())
        self.y = int(input())

    def display(self):
        print(
            f"To pay the rent amount they need to arrange : {self.rent-self.ram-self.y}Rs")


class check(hostel):
    def display(self):
        return super().display()


obj = check()
obj.display()
