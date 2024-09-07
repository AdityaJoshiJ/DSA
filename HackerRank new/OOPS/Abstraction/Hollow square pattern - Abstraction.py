from abc import ABC, abstractmethod


class patter(ABC):
    def __init__(self):
        self.m = int(input())

    @abstractmethod
    def print_hollow_square_pattern(self):
        n = self.m
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


class hollowPattern(patter):
    def print_hollow_square_pattern(self):
        return super().print_hollow_square_pattern()


obj = hollowPattern()
obj.print_hollow_square_pattern()
