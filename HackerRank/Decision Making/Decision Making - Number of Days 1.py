year = int(input())
month = int(input())
if year < 1900 or year > 9999:
    print("0")
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 Days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 Days")
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("29 Days")
            else:
                print("28 Days")
    else:
        print("28 Days")
