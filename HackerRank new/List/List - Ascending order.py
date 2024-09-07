n = int(input())
li = []
for i in range(0, n):
    m = int(input())
    li.append(m)
li.sort()
print(f"The Sorted array is:")
for i in range(0, n):
    print(li[i])
