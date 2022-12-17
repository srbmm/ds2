class SllNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Sll:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def insert_first(self, data):
        item = SllNode(data)
        if self.first is None:
            self.first = item
            self.last = item
        else:
            item.next = self.first
            self.first = item
        self.size += 1
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def traverse(self):
        temp = self.first
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def is_there(self, data):
        temp = self.first
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False


class BSTNode:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.need_sll = Sll()


class BST:
    def __init__(self):
        self.root = None
    
    def find_key(self, root, key):
        if root is None:
            return
        if root.key == key:
            return root
        if self.find_key(root.left, key) is not None:
            return self.find_key(root.left, key)
        if self.find_key(root.right, key) is not None:
            return self.find_key(root.right, key)

    def main_insert(self, data, key):
        if self.find_key(self.root, key) is None:
            self.recursive_insert(self.root, data, key)
            return
        temp = self.find_key(self.root, key)
        if temp.need_sll.is_empty():
            temp.need_sll.insert_first(temp.data)
        
        if temp.need_sll.is_there(data):
            return
        temp.need_sll.insert_first(data)
    
    def recursive_insert(self, p, data, key):
        if self.root is None:
            self.root = BSTNode(data, key)
            return
        if data < p.data:
            if p.left is None:
                p.left = BSTNode(data, key)
                return
            self.recursive_insert(p.left, data, key)
        else:
            if p.right is None:
                p.right = BSTNode(data, key)
                return
            self.recursive_insert(p.right, data, key)

    def find(self, key):
        root = self.root
        if root is None:
            return
        if root.key == key:
            return root.need_sll
        if self.find_key(root.left, key) is not None:
            return self.find_key(root.left, key)
        if self.find_key(root.right, key) is not None:
            return self.find_key(root.right, key)

    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(f'root.data == {root.data} root.key == {root.key}')
            self.inorder(root.right)


b1 = BST()
b1.main_insert(12, 15)
b1.main_insert(12, 15)
b1.main_insert(34, 1)
b1.main_insert(35, 12)
b1.main_insert(512, 335)
b1.main_insert(256, 1222)
b1.main_insert(144, 1111)

x = b1.find(15)
x.traverse()
