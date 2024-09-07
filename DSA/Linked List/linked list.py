class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        # self.top = None for stack

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
            print(f"{temp.data} --> ", end=" ")
            temp = temp.next
            if (temp == None):
                print("NULL")

    def insertBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertInBetween(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    print("Invalid position")
                    return
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def insertEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.last_node = new_node

        else:
            self.last_node.next = new_node
            self.last_node = new_node

    def deleteBegin(self):
        if self.head:
            self.head = self.head.next

    def deleteInBetween(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
        else:
            temp = self.head
            prev = 0
            for _ in range(position):
                if temp is None:
                    print("Invalid position")
                    return
                prev = temp
                temp = temp.next

            prev.next = temp.next
            temp.next = None

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
n = int(input())
for i in range(n):
    data = int(input())
    L.append(data)
L.display()
# data = int(input("Enter new Element to insert in beginning"))
# L.insertBegining(data)
# L.display()
# data2 = int(input("Enter new Element to insert in end"))
# L.insertEnd(data2)
# L.display()
# L.deleteBegin()
# L.display()
# L.deleteEnd()
# L.display()
position = int(input("Enter Index: "))
data3 = int(input("Enter Element to be insert: "))
L.insertInBetween(data3, position)
L.display()
position = int(input("Enter Index: "))
L.deleteInBetween(position)
L.display()
