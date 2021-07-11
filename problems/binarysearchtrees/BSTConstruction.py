# BST construction
# Write class for Binary Search Tree that supports insert, contains, and remove method
# Each BST node should have a value, left node, and right node

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while current is not None:
            if current.value > value:
                if current.left is None:
                    current.left = BinarySearchTree(value)
                    break
                else:
                    current = current.left
            else:
                if current.value < value:
                    if current.right is None:
                        current.right = BinarySearchTree(value)
                        break
                    else:
                        current = current.right

    def contains(self, value):
        current = self
        while current is not None:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return True
        return False
