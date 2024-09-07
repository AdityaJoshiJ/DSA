n = int(input())
li = list(map(int, input().split()))
avg = sum(li)//n
# print(avg)
t = 0
bl = []
for i in range(n):
    t = abs(li[i]-avg)
    bl.append(t)
print(sum(bl)//2)
