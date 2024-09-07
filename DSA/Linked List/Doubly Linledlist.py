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

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # def insertInBetween(self, data)

    def insertAtLast(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def deleteAtBegin(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            self.tail = None

    def deleteAtEnd(self):
        if self.head is None:
            return 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None


L = DoublyLL()
n = int(input())
for i in range(n):
    data = int(input())
    L.append(data)
L.display()
data = int(input("Enter new Element to insert in beginning"))
L.insertAtBegin(data)
L.display()
data2 = int(input("Enter new Element to insert in end"))
L.insertAtLast(data2)
L.display()
print("After deletion of first element")
L.deleteAtBegin()
L.display()
print("After deletion of last element")
L.deleteAtEnd()
L.display()

