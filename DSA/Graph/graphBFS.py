graph = {
    'a': ['b', 'c'],
    'b': ['f', 'd'],
    'c': [],
    'd': ['h'],
    'f': ['e'],
    'e': ['g'],
    'g': [],
    'h': []
}
queue = ['a']
visited = []
while queue:
    current_node = queue.pop(0)
    if current_node not in visited:
        visited.append(current_node)
    for neighbor in graph[current_node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
print(visited)
