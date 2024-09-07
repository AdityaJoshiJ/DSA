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

    def reverse(self, k):
        if self.head == None:
            return None
        temp = self.head
        next = None
        prev = None
        count = 0
        while (temp is not None and count < k):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            count += 1

        if next is not None:
            self.head.next = self.reverse(k)

        return prev


L = DoublyLL()
data = list(map(int, input().split()))
for i in range(len(data)):
    L.append(data[i])
k = int(input())
L.reverse(k)
L.display()


# class Node:

#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     # Function to initialize head
#     def __init__(self):
#         self.head = None

#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end=' ')
#             temp = temp.next
#         print()

#     def reverse(self, head, k):
#         if head == None:
#             return None
#         current = head
#         next = None
#         prev = None
#         count = 0
#         while (current is not None and count < k):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#             count += 1

#         if next is not None:
#             head.next = self.reverse(next, k)
#         return prev


# # Driver program
# llist = LinkedList()
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)

# llist.printList()
# llist.head = llist.reverse(llist.head, 4)

# print("4")
# llist.printList()

# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
