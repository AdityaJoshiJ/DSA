class number():
    def __init__(self):
        self.a = int(input())
        self.h = float(input())

    def age(self):
        print(f"Age: {self.a}")

    def hei(self):
        print(f"Heigth: {self.h}")


class element():
    def __init__(self):
        self.a = int(input())
        self.h = float(input())

    def age(self):
        print(f"Weigth : {self.a}")

    def hei(self):
        print(f"Heigth : {self.h}")


obj1 = element()
obj1.age()
obj1.hei()
