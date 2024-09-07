month = int(input())
rent = int(input())
day = int(input())
if month > 12:
    print("Invalid Input")
elif month == 12 or month == 11 or month == 4 or month == 5 or month == 6:
    print(day*rent*1.2)
else:
    print(day*rent)
