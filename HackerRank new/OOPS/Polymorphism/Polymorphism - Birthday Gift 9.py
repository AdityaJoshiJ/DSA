class number():
    def __init__(self):
        self.m = int(input())
        self.l = int(input())
        self.b = int(input())

    def mom(self):
        print(self.m+self.l)

    def dad(self):
        print(self.b)


class element():
    def __init__(self):
        self.m = int(input())
        self.l = int(input())
        self.b = int(input())

    def mom(self):
        print(self.m+self.l)

    def dad(self):
        print(self.m+self.l+self.b)


obj1 = element()
obj1.mom()
obj1.dad()
