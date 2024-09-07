str = input()
for i in range(0, len(str)):
    count = str.count(str[i])
    if count == 1:
        print(str[i])
        break
if count > 1:

    print("All the characters are repetitive")
