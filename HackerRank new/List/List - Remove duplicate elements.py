n = int(input())
li = []
for i in range(0, n):
    m = int(input())
    if m in li:
        pass
    else:
        li.append(m)
for i in range(0, len(li)):
    print(li[i])
