def print_hollow_square_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


n = int(input())

print_hollow_square_pattern(n)
