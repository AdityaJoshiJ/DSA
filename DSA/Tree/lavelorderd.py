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
        if data < Node.data:
            Node.left = self.insert(Node.left, data)
        else:
            Node.right = self.insert(Node.right, data)
        return Node

    def traversalInOrder(self, root):
        if root is not None:
            self.traversalInOrder(root.left)
            print(root.data, end=" ")
            self.traversalInOrder(root.right)

T = tree()

li = list(map(int, input("Enter Elements of TREE: ").split()))
root = li[0]
root = T.create(root)

for element in li:
    T.insert(root, element)

print(T.heightOfTree(root))
