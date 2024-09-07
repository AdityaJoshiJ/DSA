def sum_of_digits(num):
    while num > 9:
        temp = num
        digit_sum = 0
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        num = digit_sum
    return num


number = int(input())


result = sum_of_digits(number)

print(result)
