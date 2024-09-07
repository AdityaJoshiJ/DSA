x = int(input())
y = int(input())


def power(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n*power(n, p-1)


f = power(x, y)
print(f"The value of {x} power {y} is {f}")
