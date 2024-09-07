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

    def searchInorder(self, root, targetToBeSearch):
        if root is not None:
            self.searchInorder(root.left, targetToBeSearch)
            if root.data == targetToBeSearch:
                print(root.data)
            self.searchInorder(root.right, targetToBeSearch)

    def traversalPreOrder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.traversalPreOrder(root.left)
            self.traversalPreOrder(root.right)

    def searchPreOrder(self, root, targetToBeSearch):
        if root is not None:
            self.searchPreOrder(root.left, targetToBeSearch)
            self.searchPreOrder(root.right, targetToBeSearch)
            if root.data == targetToBeSearch:
                print(root.data)

    def traversalPostOrder(self, root):
        if root is not None:
            self.traversalPostOrder(root.left)
            self.traversalPostOrder(root.right)
            print(root.data, end=" ")

    def heightOfTree(self, root):
        if root is None:
            return -1
        left_height = self.heightOfTree(root.left)
        right_height = self.heightOfTree(root.right)
        return max(left_height, right_height) + 1


T = tree()
root = int(input("Enter Root Element: "))
root = T.create(root)
# print(root.data)
li = list(map(int, input("Enter Elements of TREE: ").split()))

for element in li:
    T.insert(root, element)

# T.insert(root,4)
# T.insert(root,3)
# T.insert(root,5)
# T.insert(root,10)
# T.insert(root,8)
# T.insert(root,22)
# T.insert(root,17)
# T.insert(root,30)
# T.insert(root,28)

# print("Inorder --->>")
# T.traversalInOrder(root)
# print("\nPreorder --->>")
# T.traversalPreOrder(root)
# print("\nPostorder --->>")
# T.traversalPostOrder(root)
# targetToBeSearch = int(input("Enter Element to be search: "))
# T.searchInorder(root, targetToBeSearch)
# if(T.searchInorder(root, targetToBeSearch)==None):
#     print("Element is not present in Tree")
# T.searchPreOrder(root, targetToBeSearch)

print(T.heightOfTree(root))
