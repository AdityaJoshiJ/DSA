def transposeMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed


n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

for row in matrix:
    print(" ".join(map(str, row)))

transposedMatrix = transposeMatrix(matrix)
print("Transpose matrix is:")
for row in transposedMatrix:
    print(" ".join(map(str, row)))
