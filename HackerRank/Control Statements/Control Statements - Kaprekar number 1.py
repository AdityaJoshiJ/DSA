def is_kaprekar_number(num):
    square = num**2
    digits = str(square)
    length = len(digits)

    for i in range(1, length):
        left = int(digits[:i])
        right = int(digits[i:])

        if left + right == num:
            return True

    return False


# Taking input from the user
num = int(input())

if is_kaprekar_number(num):
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
