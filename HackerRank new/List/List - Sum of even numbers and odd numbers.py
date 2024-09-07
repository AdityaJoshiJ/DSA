n = int(input())
sumEven = 0
sumOdd = 0
li = []
for i in range(0, n):
    m = int(input())
    li.append(m)
    if li[i] % 2 == 0:
        sumEven = sumEven+li[i]
    else:
        sumOdd = sumOdd+li[i]

print(f"The sum of the even numbers in the array is {sumEven}")
print(f"The sum of the odd numbers in the array is {sumOdd}")
