from abc import ABC, abstractmethod


class equilibrium(ABC):
    def __init__(self):
        self.n = int(input())
        self.l = list(map(int, input().split()))

    @abstractmethod
    def cal(self):
        li = self.l
        for i in range(0, len(li)):
            x = 0
            y = 0
            for j in range(0, i):
                x += li[j]
                # print(x)
            for k in range(i+1, len(li)):
                y += li[k]
                # print(y)
            if x == y:
                print(li[i])


class check(equilibrium):
    def cal(self):
        return super().cal()


obj = check()
obj.cal()
