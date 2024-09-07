rows = int(input())
cols = int(input())
sum = 0
mtrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    mtrix.append(row)
# print(mtrix)
for i in range(0, rows):
    for j in range(0, cols):
        if (i == 0 or i == rows-1 or i == j):
            sum = sum+mtrix[i][j]
            # print(mtrix[i][j], end=" ")
    # print()
print(f"Sum of Zig-Zag pattern is {sum}")