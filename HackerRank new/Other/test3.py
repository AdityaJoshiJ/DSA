# row, col = map(int, input().split())
# mat1 = []
# mat2 = []
# mul = []
# for i in range(row):
#     mat2.append([int(x) for x in input().split()])
#     mat2.append([int(x) for x in input().split()])
#     for j in range(col):
#         for k in range(col):
#             mul[i][j] = mat1[i][k]+mat2[k][j]
# for i in range(row):
#     for j in range(col):
#         print(mul[i][j], end=" ")
# # list=[]
# for i in range(0,row):
#     a=[]
#     for j in range(0,col):
#         a.append(j)
row, col = map(int, input().split())
mat1 = []
mat2 = []
s = []
for i in range(row):
    mat1.append([int(x) for x in input().split()])
for i in range(row):
    mat2.append([int(x) for x in input().split()])

mult = [[0 for i in range(col)] for j in range(row)]
mult2 = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        for k in range(col):
            mult[i][j] += mat1[i][k] * mat2[k][j]
for i in range(row):
    for j in range(col):
        print(mult[i][j], end=" ")
    print()
print(sum(mult[0]), sum(mult[1]), sum(mult[2]))


if sum(mult[0]) > sum(mult[1]):
    if sum(mult[0]) > sum(mult[2]):
        print(0)
    else:
        print(2)
else:
    if sum(mult[1]) > sum(mult[2]):
        print(1)
    else:
        print(2)
for j in range(col):
    for i in range(row):
        mult2[j][i] = mult[i][j]
print(sum(mult2[0]), sum(mult2[1]), sum(mult2[2]))

if sum(mult2[0]) > sum(mult2[1]):
    if sum(mult2[0]) > sum(mult2[2]):
        print(0)
    else:
        print(2)
else:
    if sum(mult2[1]) > sum(mult2[2]):
        print(1)
    else:
        print(2)
