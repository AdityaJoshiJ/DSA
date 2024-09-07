age = int(input())
year = int(input())
income = int(input())
arrears = int(input())
mark = int(input())
attenddance = int(input())
if year >= 2021 and age >= 18 and age <= 21 and mark >= 80 and income <= 250000:
    if arrears <= 2 and attenddance >= 60 and income <= 200000:
        print("Eligible")
    elif arrears > 2 and attenddance >= 90:
        print("Partially Eligible")
    else:
        print("Not Eligibl")
else:
    print("Not Eligible")
