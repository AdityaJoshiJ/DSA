n = int(input())
arr = []
b = []
sml = sum(arr)
for i in range(0, n):
    m = int(input())
    arr.append(m)
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if i == j:
            pass
        else:
            temp = abs(arr[i]-arr[j])
            b.append(temp)
    # print(b)
    t = sum(b)
    # print(t)
    if t < sml:
        sml = t
    b = []
print(sml)
