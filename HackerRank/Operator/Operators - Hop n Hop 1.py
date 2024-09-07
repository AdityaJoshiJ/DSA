import math
def calculate_hops(x, y):
    peter_house = (3, 4)
    friend_house = (x, y)

    distance = math.sqrt(pow((friend_house[0] - peter_house[0]),2) + pow((friend_house[1] - peter_house[1]),2))

    hops = int(distance)
    return hops

x = int(input())
y = int(input())
print(calculate_hops(x, y))
