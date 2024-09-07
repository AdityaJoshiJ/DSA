class mbbs:
    def __init__(self):
        self.name = input()
        self.bed = int(input())
        self.wed = int(input())
        self.dname = input()
        self.d = input()
        self.t = int(input())

    def display(self):
        print("Inserted Data")
        print(f"Patient Name : {self.name}")
        print(f"Bed Number : {self.bed}")
        print(f"Ward Name : {self.wed}")
        print(f"Doctor Name : {self.dname}")
        print(f"Doctorate Degree : {self.d}")
        print(f"Total Dues of Patient : {self.t}")


class check(mbbs):
    def display(self):
        return super().display()


obj = check()
obj.display()
