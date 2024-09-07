class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
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

    def ispalindrome(self, data):
        if self.head == None:
            return False

        temp = self.head
        tempRev = self.tail
        while temp is not None:
            if temp.data != tempRev.data:
                return False
            temp = temp.next
            tempRev = tempRev.prev
        return True


L = DLL()
n = int(input())
for i in range(n):
    data = int(input())
    L.append(data)

print(L.ispalindrome(data))
