# function that takes non empty, sorted array of distinct integers
# construct BST from integers and return root
# should minimize height
# provided with a BST class

# i want to go to the middle of the array and insert the value
# keep that as the root of the BST to be returned
# recurse on the left child with the midpoint from left subarray
# recurse on the right child with the right subarray
# base case: if the the array is empty then return

def minHeightBst(array):
    if len(array) == 0:
        return

    mid = int(len(array) / 2)
    root = BST(array[mid])
    root.left = minHeightBst(array[0:mid])
    root.right = minHeightBst(array[mid+1: len(array)])

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
