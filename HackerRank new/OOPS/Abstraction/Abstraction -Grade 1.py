from abc import ABC, abstractmethod


class school(ABC):
    def __init__(self):
        self.name = input()
        self.sAge = int(input())
        self.sGender = input()
        self.totalM = int(input())

    @abstractmethod
    def show(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.sAge}")
        print(f"Gender:{self.sGender}")
        print(f"TotalMarks:{self.totalM}")
        print(f"Percentage:{self.totalM/5}")
        per = self.totalM/5
        if per > 90:
            print("Grade:A")
        elif per > 80:
            print("Grade:B")
        elif per > 70:
            print("Grade:c")
        elif per > 60:
            print("Grade:D")
        else:
            print("Grade:F")


class student(school):
    def show(self):
        return super().show()


obj = student()
obj.show()
