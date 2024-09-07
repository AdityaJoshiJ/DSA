class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return 0
        else:
            d = self.top.data
            self.top = self.top.next
            print(d)
    
    def peek(self):
        if self.top:
            print(self.top.data)
        else:
            print("Stack is Empty")

    def display(self):
        temp = self.top
        while temp is not None:
            print(f"{temp.data}", end=" ")
            temp = temp.next


S = Stack()
data = list(map(int, input().split()))
for i in range(len(data)):
    S.push(data[i])

S.peek()
S.pop()
S.peek()
S.display()
