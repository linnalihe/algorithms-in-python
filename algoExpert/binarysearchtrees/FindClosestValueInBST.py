# Find closest value in BST
# Given root node of BST and a target, find the closest value to the target value

# keep track of the closest value to the target, need to return this
# keep track of the difference for checking how close to target, absolute difference
# keep track of the current value
# initialize closest, diff, and current to the first node of the tree
def findClosestValueInBst(tree, target):
    closest = tree.value
    diff = abs(target-closest)
    current = tree
    while current is not None:
        currentDiff = abs(target - current.value)
        if currentDiff < diff:
            closest = current.value
            diff = abs(target - closest)

        if target > current.value:
            current = current.right
        elif target < current.value:
            current = current.left
        elif target == current.value:
            return current.value

    return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
