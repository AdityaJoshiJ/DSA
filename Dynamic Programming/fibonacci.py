#   Tabulation: Buttom up

def fib(position):
    if position <= 2:
        return 1
    d = [0]*position
    d[0] = 1
    d[1] = 1
    for i in range(2, position):
        d[i] = d[i-1]+d[i-2]
    print(d[-1])


fib(9)

#  memoization: Top down


def fib(position, memory):
    if position in memory:
        return memory[position]

    if position <= 2:
        return 1

    memory[position] = fib(position-1, memory)+fib(position-2, memory)
    return memory[position]


result = fib(4, {})
print(result)
