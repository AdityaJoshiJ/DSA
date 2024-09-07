class car:
    def __init__(self, name, model, topSpeed, price):
        self.name = name
        self.model = model
        self.topSpeed = topSpeed
        self.price = price

    def applyBreak(self):
        print("You have to appily break")

    def increseSpeed(self):
        print("You can increse Speed Up to 300Km/h")


obj1 = car("Aston martin", "ValKyris", 402, "3 Cr.")
obj2 = car("Bugatti", "Chiron", 489, "20 Cr.")
obj1.applyBreak()
obj1.increseSpeed()
