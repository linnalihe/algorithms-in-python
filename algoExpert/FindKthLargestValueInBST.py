# Find Kth Largest Value in BST

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# need to keep track of the numbers in the tree
# brute force would be to move everything into an array
# with binary search trees inorder traversal will return in sorted order
# and then return index of len(elements) - k

# the node is the mid point for the array
# the left most node is index 0
# the right most node is index of len(elements)

# you can inorder traverse in reverse and keep track of k


def findKthLargestValueInBst(tree, k):

    # indexAndValue[0] keeps track of k and indexAndValue[1] keeps track of value
    indexAndValue = [0, -1]
    reverseTraverse(tree, k, indexAndValue)

    return indexAndValue[1]


def reverseTraverse(tree, k, indexAndValue):

    if tree == None or indexAndValue[0] >= k:
        return

    reverseTraverse(tree.right, k, indexAndValue)
    if indexAndValue[0] < k:
        indexAndValue[0] += 1
        indexAndValue[1] = tree.value
        reverseTraverse(tree.left, k, indexAndValue)
