from abc import ABC, abstractmethod


class duck(ABC):
    def __init__(self):
        self.n = int(input())

    @abstractmethod
    def ducknumber(self):
        x = self.n
        while x > 9:
            a = x % 10
            if a == 0:
                return "Duck Number"
                break
            else:
                x = x//10


class soni(duck):
    def ducknumber(self):
        return super().ducknumber()


obj = soni()
print(obj.ducknumber())
