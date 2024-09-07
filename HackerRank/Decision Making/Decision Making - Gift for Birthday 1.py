b = int(input())
if (b % 4 == 0 and b % 100 != 0) or (b % 400 == 0):
    print(f"{b} is a leap year")
else:
    print(f"{b} is not a leap year")
