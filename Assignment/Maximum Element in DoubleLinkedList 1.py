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
        print("NULL", end=" ")
        while temp is not None:
            print(f"<--{temp.data}-->", end=" ")
            temp = temp.next
            if (temp == None):
                print("NULL")

    def maxelement(self):
        maximun = 0
        temp = self.head
        while temp is not None:
            if maximun <= temp.data:
                maximun = temp.data
            temp = temp.next
        print(maximun)


L = DoublyLL()
data = list(map(int, input().split()))
for i in range(len(data)):
    L.append(data[i])
L.maxelement()
