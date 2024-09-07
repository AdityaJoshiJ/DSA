l = int(input())
arr = list(map(int, input().split()))
n = int(input())
m = int(input())
for i in range(0, l):
    if arr[i]-n < m:
        arr[i] = arr[i]+1
print(arr)

# arr = list(map(int, input().split()))
# i = 0
# count = 0
# for i in range(0, len(arr), arr[i]+i):
#     count += 1
# print(count)
