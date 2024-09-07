# import math
# import random


# def cardGen():
#     n = random.random()
#     ranCard = math.floor(n*pow(10, 16)+1)
#     even = 0
#     odd = 0
#     temp = ranCard
#     while temp > 0:
#         odd += temp % 10
#         temp = temp//10
#         even += temp % 10
#         temp = temp//10
#     if (odd*2+even) % 10 == 0:
#         return ranCard
#     else:
#         return cardGen()


# print(cardGen())>

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
for i in range(0, len(nums)):
    if i not in nums:
        print(i)
