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

    def check(self, element):
        temp = self.head
        i = 0
        while temp is not None:
            if temp.data == element:
                print(i)
                return
            else:
                i += 1
            temp = temp.next

        print("-1")


data = list(map(int, input().split()))
element = int(input())

L = DoublyLL()
for i in data:
    L.append(i)

L.check(element)
