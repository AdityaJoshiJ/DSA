from abc import ABC, abstractmethod


class meating(ABC):
    def __init__(self):
        self.n = int(input())

    @abstractmethod
    def totalHandShake(self):
        m = self.n-1
        print(int((m*(m+1))/2))


class handShake(meating):
    def totalHandShake(self):
        return super().totalHandShake()


obj = handShake()
obj.totalHandShake()
