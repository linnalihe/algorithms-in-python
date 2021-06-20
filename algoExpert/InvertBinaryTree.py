# takes a binary tree, input is the root node
# invert it - swap every left node for it's corresponding right node
# children nodes can be nodes or they can be None/null
# will there always be a left node? if there is a right node?

# approach 1:
# at each node swap the left child with the right child
# if the node has a right child but no left child make left child = right child and right child = null
# but swapping them will solve this so it doesn't matter if either children are null
# recurse on the left and the right child
# base case is if the node does not have right or left children
# vis versa for the left child

def invertBinaryTree(tree):
    if(tree is None):
        return

    tree.left, tree.right = tree.right, tree.left

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

# for an iterative solution you have to use a queue
# push the node onto the queue and swap the left and right children


def invertBinaryTree2(tree):
    queue = [tree]

    while queue:
        current = queue.pop()
        if current is None:
            continue
        current.right, current.left = current.left, current.right
        queue.append(current.right)
        queue.append(current.left)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
