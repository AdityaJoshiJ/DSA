def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


n = int(input())
m = int(input())

result = gcd(n, m)
print(result)
