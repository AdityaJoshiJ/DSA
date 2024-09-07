n = ""
str = []
while n != "####":
    n = input()
    if n != "####":
        str.append(n)

temp = 0
# print(len(str))
print(str[0])
for i in range(1, len(str)):
    temp = str[i-1]
    temp2 = str[i]

    lC = temp[-1]
    fC = temp2[0]
    if lC == fC:
        print(str[i])
    # print(temp)
