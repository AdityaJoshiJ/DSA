# # without recuration 
# n = [2, 5, 7, 4, 9, 1]
# gtr = 0
# for i in range(0, len(n)):
#     if n[i] > gtr:
#         gtr = n[i]
# print(gtr)
n = int(input())
arr = []
for i in range(0, n):
    m = int(input())
    arr.append(m)


def maxvalue(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], maxvalue(arr, n-1))


y = maxvalue(arr, n)
print(f"Maximum element in the array is {y}")
