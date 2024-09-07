class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}", end=" ")
            temp = temp.next

    def insertInBetween(self, data, position):
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node


L = DoublyLL()
data = list(map(int, input().split()))
for i in data:
    L.append(i)

position, element = map(int, input().split())
L.insertInBetween(element, position)
L.display()
