n = int(input())
li = []
for i in range(0, n):
    m = int(input())
    li.append(m)
location = int(input())
if location-1 > len(li):
    print("Invalid Input")
else:
    element = int(input())
    li.insert(location-1, element)
    print("Array after insertion is")
    for i in range(0, len(li)):
        print(li[i])
