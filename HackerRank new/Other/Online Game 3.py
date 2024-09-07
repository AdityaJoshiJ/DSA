# n = int(input())
# li = []
# liEven = []
# liOdd = []
# m = list(map(int, input().split()))
# li = m
# for i in range(0, n):
#     if li[i] % 2 == 0:
#         liEven.append(li[i])
#     else:
#         liOdd.append(li[i])
# liEven.extend(liOdd)
# print("Array after Segregation")
# for i in range(0, len(liEven)):
#     print(liEven[i], end=" ")

# Code of Bhamareji
num = int(input())
arr = list(map(int, input().split()))
start = 0
end = num - 1
while start < end:
    while start < num and arr[start] % 2 == 0:
        start += 1
    while end >= 0 and arr[end] % 2 != 0:
        end -= 1
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
print("Array after Segregation")
print(*arr)
