# Easy

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]


# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Runtime: 36 ms, faster than 32.62% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 14.1 MB, less than 83.30% of Python3 online submissions for Binary Tree Paths.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# implement recursive depth-first search
# keep track of a string path
# if you get to a leaf, append it to the output
class Solution:

    def binaryTreePathsHelper(self, root: TreeNode, nodesList: list, pathStr: str) -> None:
        if root == None:
            return
        else:

            if root.left or root.right:
                pathStr += (str(root.val)+"->")
            else:
                pathStr += (str(root.val))
                nodesList.append(pathStr)

            self.binaryTreePathsHelper(root.left, nodesList, pathStr)
            self.binaryTreePathsHelper(root.right, nodesList, pathStr)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        nodesList = []
        pathStr = ""

        self.binaryTreePathsHelper(root, nodesList, pathStr)

        return nodesList


class Solution2:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        output = []
        # stack of node contains tuple with node and it's value
        nodeStack = [(root, str(root.val))]
        while nodeStack:
            currentNode, path = nodeStack.pop()
            if not currentNode.left and not currentNode.right:
                output.append(path)
            if currentNode.right:
                nodeStack.append(
                    (currentNode.right, path+"->"+str(currentNode.right.val)))
            if currentNode.left:
                nodeStack.append(
                    (currentNode.left, path+"->"+str(currentNode.left.val)))

        return output
