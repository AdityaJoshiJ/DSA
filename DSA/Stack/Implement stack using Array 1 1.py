n = int(input())
i = 0
li = []


while i != n:
    t = input()
    if t == "Push":
        x = int(input())
        li.append(x)
    elif t == "Pop":
        li.pop()
    elif t == "Print":
        for j in range(len(li)):
            print(li[j])

    i += 1
