def find(li):
    n = len(li)
    j = 0
    for i in range(n):
        if li[i] <= 0:
            li[i], li[j] = li[j], li[i]
            j += 1
    positive_nums = li[j:]
    # Mark the presence of a number by making the corresponding index negative
    for num in positive_nums:
        index = abs(num) - 1
        if index < len(positive_nums):
            positive_nums[index] = -abs(positive_nums[index])

    # Find the smallest positive number that is not marked
    for i in range(len(positive_nums)):
        if positive_nums[i] > 0:
            return i + 1

    # If all positive numbers are present, return the next positive integer in sequence
    return len(positive_nums) + 1


n = int(input())
li = list(map(int, input().split()))
result = find(li)
print(result)
