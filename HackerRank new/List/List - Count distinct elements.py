n = int(input())
li = []
for i in range(0, n):
    m = int(input())
    li.append(m)
newList = set(li)
print(f"There are {len(newList)} distinct element in the array.")
