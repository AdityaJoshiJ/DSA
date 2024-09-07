class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class dL:
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
            new_node.previous = self.tail
            self.tail = new_node

    def Display(self):
        if self.head is None:
            return -1
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    def duplicates(self):
        if self.head is None:
            return

        temp = self.head

        while temp:
            temp1 = temp
            while temp1.next:
                if temp1.next.data == temp.data:
                    temp1.next = temp1.next.next
                else:
                    temp1 = temp1.next
            temp = temp.next


L = dL()
n = int(input())
li = list(map(int, input().split()))
for i in range(len(li)):
    L.append(li[i])
L.duplicates()
L.Display()
