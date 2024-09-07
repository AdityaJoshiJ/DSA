def move(num):
    num = list(str(num))
    zeroes = [i for i in num if i == '0']
    ones = [i for i in num if i != '0']
    result = ones + zeroes
    return int(''.join(result))


T = int(input())
for i in range(T):
    n = int(input())
    result = move(n)
    print(result)
