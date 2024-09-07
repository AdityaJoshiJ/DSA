class student:
    def __init__(self):
        self.name = input()
        self.rNo = int(input())
        self.m = int(input())
        print("Enter name:")
        print("Enter roll number:")
        print("Enter total marks out of 500:")
        print("Student details:")
        print(f"Name:{self.name}")
        print(f"Roll Number:{self.rNo}")
        print(f"Total:{self.m}")
        print(f"Percentage:{self.m/5}")


ob = student()
