class sum:
    def __init__(self):
        self.n = int(input())
        s = 0
        for i in range(1, self.n):
            if i % 2 == 0:
                pass
            else:
                s = s+i
        print(s)


f = sum()
