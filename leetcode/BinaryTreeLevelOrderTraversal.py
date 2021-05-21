
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        output = []  # list of arrays where each array is a level
        subarray = []
        nodeQueue = deque()
        level = 0
        nodeQueue.append((level, root))

        while nodeQueue:

            index, node = nodeQueue.popleft()
            if(index > level):
                output.append(subarray)
                subarray = []
                level += 1
            subarray.append(node.val)

            if node.left:
                nodeQueue.append((index+1, node.left))
            if node.right:
                nodeQueue.append((index+1, node.right))

        output.append(subarray)

        return output
