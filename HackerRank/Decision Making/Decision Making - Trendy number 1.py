n = int(input())
if n/100 < 1:
    print("Invalid Number")
else:
    n = n//10
    n = n % 10
    if n % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
