class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class tree:
    def create(self, data):
        return Node(data)

    def insert(self, Node, data):
        if Node is None:
            return self.create(data)
        if data <= Node.data:
            Node.left = self.insert(Node.left, data)
        else:
            Node.right = self.insert(Node.right, data)
        return Node

    def displayInOrder(self, root):
        if root is not None:
            print(f"{root.data}:", end="")
            if root.left is not None:
                print(f"L:{root.left.data},", end="")
            if root.right is not None:
                print(f"R:{root.right.data}", end="")
            print("")
            self.displayInOrder(root.left)
            self.displayInOrder(root.right)

    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if root.data < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root


T = tree()
n = int(input())
f = 0
for i in range(n):
    li = list(map(int, input().split()))
    # print(li)
    if li[0] == 1:
        if f == 0:
            root = T.create(li[1])
            f = 1
        else:
            T.insert(root, li[1])
    elif li[0] == 3:
        if T.search(root, li[1]):
            print("true")
        else:
            print("false")
    elif li[0] == 2:
        T.delete(root, li[1])
    elif li[0] == 4:
        T.displayInOrder(root)
