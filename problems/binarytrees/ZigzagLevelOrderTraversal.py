# Leetcode
# Medium

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Runtime: 32 ms, faster than 71.80% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14.5 MB, less than 72.89% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        ret = []
        nodeQueue = [root]
        level = 0
        while nodeQueue:
            levelQueue = []
            for _ in range(len(nodeQueue)):
                currNode = nodeQueue.pop(0)
                levelQueue.append(currNode.val)
                if currNode.left:
                    nodeQueue.append(currNode.left)
                if currNode.right:
                    nodeQueue.append(currNode.right)

            if levelQueue and level % 2 == 0:
                ret.append(levelQueue)
            elif levelQueue:
                ret.append(reversed(levelQueue))

            level += 1

        return ret


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        ret = []
        RightToLeft = [root]
        LeftToRight = []

        while True:
            levelNodes = []
            while RightToLeft:
                currNode = RightToLeft.pop()
                levelNodes.append(currNode.val)
                if currNode.left:
                    LeftToRight.append(currNode.left)
                if currNode.right:
                    LeftToRight.append(currNode.right)

            if levelNodes:
                ret.append(levelNodes)

            levelNodes = []
            while LeftToRight:
                currNode = LeftToRight.pop()
                levelNodes.append(currNode.val)
                if currNode.right:
                    RightToLeft.append(currNode.right)
                if currNode.left:
                    RightToLeft.append(currNode.left)

            if levelNodes:
                ret.append(levelNodes)

            if(not RightToLeft and not LeftToRight):
                break

        return ret
