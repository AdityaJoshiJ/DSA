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

    def evenodd(self, data):
        li = []
        li1 = []
        li2 = []
        temp = self.head
        while temp is not None:
            if temp.data % 2 == 0:
                li.append(temp.data)
                temp = temp.next
            else:
                li1.append(temp.data)
                temp = temp.next
        li2 = li1+li
        return li2


L = LL()
data = list(map(int, input().split()))
for i in data:
    L.append(i)
# L.display()
L2 = LL()
aj = L.evenodd(data)
for i in aj:
    L2.append(i)
L2.display()
