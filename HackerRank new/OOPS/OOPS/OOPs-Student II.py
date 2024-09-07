class student:
    def __init__(self):
        self.name = input()
        self.rNo = int(input())
        self.att = int(input())

    def show(self):
        print(self.name)
        print(self.rNo)
        print(f"{self.att}%")


class sec:
    def __init__(self):
        ob = student()
        ob.show()


ob1 = sec()
