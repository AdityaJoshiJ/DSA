class bill:
    def __init__(self):
        self.n = int(input())
        self.na = input()
        self.u = int(input())
        print(self.n)
        print(self.na)
        print(self.u)
        if self.u <= 100:
            print(int(self.u*1.2))
        elif self.u <= 300:
            print((self.u-100)*2+120)
        else:
            print((self.u-300)*3+520)


ans = bill()
