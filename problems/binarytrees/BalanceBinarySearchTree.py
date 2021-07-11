# Leetcode
# medium

# Given a binary search tree, return a balanced binary search tree with the same node values.

# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

# If there is more than one answer, return any of them.

# Example 1:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.


# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Your runtime beats 55.90 % of python3 submissions.
# Your memory usage beats 55.37 % of python3 submissions.
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        listOfNodes = []
        self.traverseTree(root, listOfNodes)
        listOfNodes.sort()

        return self.listToBST(listOfNodes, 0, len(listOfNodes))

    def traverseTree(self, root, listOfNodes):

        if root is None:
            return []
        else:
            listOfNodes.append(root.val)
            self.traverseTree(root.right, listOfNodes)
            self.traverseTree(root.left, listOfNodes)

    def listToBST(self, listOfNodes, a, b):

        if a >= b:
            return None

        mid = int(a+(b-a)/2)
        newTree = TreeNode(listOfNodes[mid])
        newTree.left = self.listToBST(listOfNodes, a, mid)
        newTree.right = self.listToBST(listOfNodes, mid+1, b)
        return newTree


# binary search tree
# left children is always smaller then parent
# right children always larger than parent
# depth of 2 subtrees - nodes on same level don't differ by 1

# approach 1:
# create a sorted array of the nodes
# then create a binary search tree from the sorted array, starting from the midpoint?


# iterative in-order-traversal
# need a stack list
# need a visited list
# need a result list
