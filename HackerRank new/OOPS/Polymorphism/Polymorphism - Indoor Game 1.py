class number():
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())

    def one(self):
        print(self.a)

    def two(self):
        print(self.b)


class element():
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())

    def one(self):
        print(self.a**2)

    def two(self):
        print(self.b*self.c)


obj1 = element()
obj1.one()
obj1.two()
