def convert(input):
    row = (input - 1) // 3
    col = (input - 1) % 3
    return row, col


input_num = int(input())
row, col = convert(input_num)
print(row, col)
