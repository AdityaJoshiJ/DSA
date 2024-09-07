class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node = new_node

        else:
            self.last_node.next = new_node
            self.last_node = new_node

    def maxelement(self):
        maximun = 0
        temp = self.head
        while temp is not None:
            if maximun <= temp.data:
                maximun = temp.data
            temp = temp.next
        print(maximun)


L = LL()
n = 5
for i in range(n):
    data = int(input())
    L.append(data)
L.maxelement()
