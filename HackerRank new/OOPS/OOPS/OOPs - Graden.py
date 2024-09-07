import math as m


class cir:
    def __init__(self):
        self.r = int(input())
        print("Enter the value of Radius :")
        print(f"Area of Circle : {3.14*pow(self.r, 2)}")


big = cir()