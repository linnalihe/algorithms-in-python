# Minimum Tree
# Given a sorted array with unique integer elements, create a binary tree with minimal height

def createMinimalBST(arr: list):
    return createMinimalBST(arr, 0, len(arr) - 1)


def createMinimalBST(arr: list, start: int, end: int):
    if(end < start):
        return None

    mid = (start + end) / 2
    n = TreeNode(arr[mid])
    n.left = createMinimalBST(arr, start, mid - 1)
    n.right = createMinimalBST(arr, mid+1, end)
    return n


class TreeNode:
    pass
