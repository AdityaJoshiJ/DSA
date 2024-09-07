from abc import ABC, abstractmethod


class number(ABC):
    def __init__(self):
        self.num = int(input())

    # concrete method
    def display(self):
        print("Enter the Number: ")

    @abstractmethod
    def isperfect(self):
        divisors = 0
        for i in range(1, self.num):
            if self.num % i == 0:
                divisors += i
        if divisors == self.num:
            print("Yes")
        else:
            print("No")


class check(number):
    def isperfect(self):
        super().isperfect()
        pass


obj = check()
obj.isperfect()
obj.display()
