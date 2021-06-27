# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    flat = inorderArray(root, [])
    leftmost = flat[0]
    for idx in range(len(flat)):
        if idx == 0:
            curr = leftmost
        else:
            curr.right = flat[idx]
            curr.right.left = curr
            curr = curr.right
    return leftmost


def inorderArray(root, arr):

    if root is None:
        return None

    inorderArray(root.left, arr)
    arr.append(root)
    inorderArray(root.right, arr)

    return arr

# [2, 6, 3, 5, 4, 7, 1]
#leftmost = 2
# curr = leftmost
# idx = 1, curr.right = 6, 6 => 2 | curr = 6
# idx = 2, curr.right = 3, 3 => 6 | curr = 3
# curr = 7
# idx = 6, curr.right = 1,
#        5
#     /    \
#    6      7
#   / \    /  \
#  2   3  4   1

# return 2
# 2 <-> 6 <-> 3 <-> 5 <-> 4 <-> 7 <-> 1


# inorder traverse this tree, if no children
# create a node, pass it to the next recursive step

# inorder traverse the binary tree and the nadd each node to the array
# iterate through the array and create the doubly linked list
