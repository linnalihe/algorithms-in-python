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


def findClosestValueInBst2(tree, target):

    return findClosestValue(tree, target, tree.value)


def findClosestValue(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestValue(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValue(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBst3(tree, target):
    closest = tree.value
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
