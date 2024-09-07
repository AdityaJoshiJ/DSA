s = int(input())
li = list(map(int, input().split()))
n = int(input())
arr = []
i = 0
j = 2
while i <= n:
    if j % 2 == 0 or j % 3 == 0 or j % 5 == 0:
        arr.append(j)
        j += 1
        i += 1
    else:
        j += 1
print(arr[n-1])
 