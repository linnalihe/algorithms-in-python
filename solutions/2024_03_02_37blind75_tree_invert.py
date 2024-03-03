# https://leetcode.com/problems/invert-binary-tree/
# all tests passed
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None
    
    temp = root.right
    root.right = root.left
    root.left = temp
    self.invertTree(root.right)
    self.invertTree(root.left)

    return root