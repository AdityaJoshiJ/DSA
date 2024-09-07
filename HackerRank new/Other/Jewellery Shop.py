m = int(input())
n = int(input())
count = 0


def divisor(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return set(div)


def prime(n):
    # Check if the number is less than
    # or equal to 1, return False if it is
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):

        if n % i == 0:
            return False

    return True


for i in range(m, n+1):
    flag = False
    z = divisor(i)
    # print(len(z))
    flag = prime(len(z))
    if flag == True:
        count += 1
    # print(flag)
print(count)
