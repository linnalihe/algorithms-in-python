# https://leetcode.com/problems/validate-binary-search-tree/
# all tests passed
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check_valid(root, leftbound, rightbound):
            if not root:
                return True

            if not (root.val > leftbound and root.val < rightbound):
                return False
            
            return check_valid(root.left, leftbound, root.val) and check_valid(root.right, root.val, rightbound)

        return check_valid(root, float("-inf"), float("inf"))