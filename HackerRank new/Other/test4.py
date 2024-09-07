# Q-1 find sum of Integer
# n = int(input())
# b = 0
# while n % 10 != 0:
#     a = n % 10
#     n = n//10
#     b = b+a
# print(b)


# Q-2 Find rew of interger
# n = int(input())
# p = n
# count = -1
# while p % 10 != 0:
#     count += 1
#     p = p//10
# a = 0
# while n % 10 != 0:
#     a = a+(n % 10)*(10**count)
#     n = n//10
#     count -= 1
# print(a)

# Q-3 Give First n prime number
# def is_prime(n):
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             return False
#     return True


# def find_prime_numbers(n):
#     primes = []
#     for num in range(3, n + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes


# num = int(input())

# primes = find_prime_numbers(num)
# print(*primes)


# Q-4 sift all zero first in list

t = int(input())


def move(m):
    m = list(str(m))
    zero = [i for i in m if i == '0']
    not_zero = [i for i in m if i != '0']
    result = zero+not_zero
    return result


for i in range(0, t):
    n = int(input())
    result = move(n)
    print(result)
