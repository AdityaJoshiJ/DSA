dict = {
    'a': ['b', 'c'],
    'b': ['f', 'd'],
    'c': [],
    'd': ['h'],
    'f': ['e'],
    'e': ['g'],
    'g': [],
    'h': []
}
stack = ['a']
v = []
# start=input()
while stack:
    currentNode = stack[-1]
    if currentNode not in v:
        v.append(currentNode)
    stack.pop()
    for values in dict[currentNode]:
        if values not in v:
            stack.append(values)

print(v)
