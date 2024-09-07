from abc import ABC, abstractmethod


class remove(ABC):
    def __init__(self):
        self.n = input()
        self.m = input()

    @abstractmethod
    def chang(self):
        for i in self.m:
            if i not in self.n:
                print(i, end="")


class check(remove):
    def chang(self):
        return super().chang()


obj = check()
obj.chang()
