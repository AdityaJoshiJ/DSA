n = int(input())
arr = []
for i in range(0, n):
    m = int(input())
    arr.append(m)
# print(arr)

s = 0


def sum(a, n):
    if len(a) == 0:
        return a[n]
    elif n >= 0:
        return a[n]+sum(a, n-1)
    else:
        return 0

f = sum(arr, n-1)
print(f)