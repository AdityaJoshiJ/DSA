n = abs(int(input()))
board = list(map(int, input().split()))
blank = []
count = 0
j = []
for i in range(0, n):
    j.append(i+1)
org = j
# print(org)
flag = True
while flag:
    for i in range(0, n):
        blank.append(j[board[i]-1])
    # print(blank)
    j = blank
    # print(j)
    blank = []
    count += 1
    if (org == j):
        flag = False
print(count)
