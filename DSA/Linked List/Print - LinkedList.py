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

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}", end=" ")
            temp = temp.next

    def deleteEnd(self):
        if self.head:
            temp = self.head
            previous = 0
            while temp.next:
                previous = temp
                temp = temp.next
            if previous:
                previous.next = None
            else:
                self.head = None


L = LL()
data = list(map(int, input().split()))
for i in data:
    L.append(i)
L.deleteEnd()
L.display()
