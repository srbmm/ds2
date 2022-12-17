class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def _add(self, root, node):
        if self.root is None:
            self.root = node
            return
        if node.value < root.value:
            if root.left is None:
                root.left = node
                return
            self._add(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return
            self._add(root.right, node)

    def insert(self, value):
        temp = Node(value)
        self._add(self.root, temp)
        return temp

    def res(self, root, root1, root2):
        self.find(root, root1)
        print(root.value, end=", ")
        self.rec_find(root, root2)

    def find(self, root, value):
        if root is None:
            return
        if root.value == value:
            return root
        if self.find(root.left, value) is not None:
            print(root.left.value, end=", ")
            return root
        if self.find(root.right, value) is not None:
            print(root.right.value, end=", ")
            return root

    def rec_find(self, root, value):
        if root is None:
            return
        if root.value == value:
            return root
        if root.right is not None:
            print(root.right.value, end=", ")
            self.rec_find(root.right, value)
            return root
        if root.left is not None:
            print(root.left.value, end=", ")
            self.rec_find(root.left, value)
            return root


test = BinaryTree()
test.insert(47)
test.insert(51)
test.insert(9)
test.insert(21)
test.insert(52)
test.insert(14)
test.insert(15)
test.res(test.root, 15, 52)





