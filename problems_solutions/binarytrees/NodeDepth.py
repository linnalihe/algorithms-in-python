# Node Depths
# Given a Binary tree, return the sum of all the nodes depth

# at each level, increment depth by 1
# add the depth to the a list
# sum all the depths together

# O(n) time, #O(n) space
# Iterative solution
def nodeDepths(root):
    sumlist = []
    addDepth(root, sumlist, 0)
    return sum(sumlist)


def addDepth(root, sumlist, depth):

    if root is None:
        return

    sumlist.append(depth)
    addDepth(root.left, sumlist, depth+1)
    addDepth(root.right, sumlist, depth+1)

# O(n) time, O(h) space where h is the height of binary tree
# Recursive solution


def nodeDepths2(root):
    depth = 0
    return getDepthSums(root, depth)


def getDepthSums(root, depth):

    if root is None:
        return 0
    return depth + getDepthSums(root.left, depth+1) + getDepthSums(root.right, depth+1)

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
