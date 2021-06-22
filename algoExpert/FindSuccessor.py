# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor2(tree, node):
    match = findSuccessorHelp2(tree, node, [])
    for i in range(len(match)):
        if node == match[i] and i+1 < len(match):
            return match[i+1]

    return None


def findSuccessorHelp2(tree, node, match):
    if tree == None:
        return match
    findSuccessorHelp2(tree.left, node, match)
    match.append(tree)
    findSuccessorHelp2(tree.right, node, match)

    return match

# given binary tree and a node, find the given node's successor
# nodes in binary tree have additional pointer to parent
# successor - next node in an inorder traversal
# no successor if it's last node to be visited in inorder traversal

# do an inorder traversal and if the node
# you are looking for is found, toggle a boolean
# return the next value you traverse

# 6 -> 4 -> 2 -> 5 match=true -> 1 (return)
