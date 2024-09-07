n = int(input())
m = int(input())
for i in range(n, m+1):
    a = i % 10
    b = i//10
    if (a+b)+(a*b) == i:
        print(i)
