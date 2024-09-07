def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def is_strong_number(num):
    temp = num
    sum_of_factorials = 0
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10

    if sum_of_factorials == num:
        return "Yes"
    else:
        return "No"


num = int(input())
print(is_strong_number(num))
