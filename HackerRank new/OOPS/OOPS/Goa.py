class Goa:
    def _init_(self):
        self.name = input()
        self.id = int(input())
        self.age = int(input())
        self.college = input()

    def party(self):
        print("Name:", self.name)
        print("id:", self.id)
        print("Age:", self.age)
        print("College:", self.college)
        print("I'm going for party\n")

    def education(self):
        print("Name:", self.name)
        print("id:", self.id)
        print("Age:", self.age)
        print("College:", self.college)
        print("I'm going for Education")


obj1 = Goa()
obj1.party()
obj2 = Goa()
obj2.education()
