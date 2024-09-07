n = int(input())


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(n)
print(f"The term {n} in the Fibonacci series is {result}")
