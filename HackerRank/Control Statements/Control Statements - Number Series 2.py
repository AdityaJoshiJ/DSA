n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        print((i**2)-2, end=" ")
    else:
        print((i**2)-1, end=" ")
