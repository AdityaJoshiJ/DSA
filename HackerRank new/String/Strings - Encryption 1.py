e = list(str(input()))


for i in range(0, len(e) - 1, 2):
    e[i], e[i + 1] = e[i + 1], e[i]
# e[0], e[1] = e[1], e[0]
# e[2], e[3] = e[3], e[2]
for i in e:
    print(i, end="")
