# Branch Sums
# Given a binary Tree, return list of branch sums ordered from leftmost to rightmost

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    output = []
    getBranchSum(root, 0, output)
    return output


def getBranchSum(root, currentSum, output):
    if root is None:
        return

    # always add the value of current node
    currentSum += root.value
    # once you get to the end of the branch - end of branch is when there are no right or left children
    if root.right is None and root.left is None:
        output.append(currentSum)

    # traverse the graph from left to right
    getBranchSum(root.left, currentSum, output)
    getBranchSum(root.right, currentSum, output)
