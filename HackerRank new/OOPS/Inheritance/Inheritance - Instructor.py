class employee:
    def __init__(self):
        self.n = int(input())
        self.id = int(input())
        self.name = input()
        self.subName = input()
        self.teacherName = input()
        self.deptName = input()

    def show(self):
        print(f"Id :  {self.id}")
        print(f"Name :  {self.name}")
        print(f"Subject Name  :  {self.subName}")
        print(f"Teacher Name  :  {self.teacherName}")
        print(f"Department Name :  {self.deptName}")


class schoolData(employee):
    def show(self):
        return super().show()


class allData(schoolData, employee):
    def nothing():
        print("nothing")


obj = allData()
obj.show()
