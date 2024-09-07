class mbbs:
    def __init__(self):
        self.n = int(input())
        self.no = int(input())
        self.na = input()
        self.des = input()
        self.bp = int(input())
        self.hra = int(input())
        self.da = int(input())
        self.pf = int(input())

    def display(self):
        print("e_no      e_name     des      bp      hra      da      pf      np")
        print(f"{self.no}    {self.na}    {self.des}    {self.bp}    {self.hra}    {self.da}    {self.pf}    {self.bp+self.da}")


class check(mbbs):
    def display(self):
        return super().display()


obj = check()
obj.display()
