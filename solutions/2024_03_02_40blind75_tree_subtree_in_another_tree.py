# https://leetcode.com/problems/subtree-of-another-tree/
# all tests passed
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
    if root.val == subRoot.val:
        found_subtree = self.isSame(root, subRoot)
        if found_subtree:
            return True
    
    found_left = False
    found_right = False
    if root.left:
        found_left = self.isSubtree(root.left, subRoot)
    if root.right:
        found_right = self.isSubtree(root.right, subRoot)

    return found_left or found_right

def isSame(self, treeroot1, treeroot2):
    
    if not treeroot1 and not treeroot2:
        return True

    if (not treeroot1 and treeroot2) or (treeroot1 and not treeroot2) or treeroot1.val != treeroot2.val:
        return False

    return self.isSame(treeroot1.left, treeroot2.left) and self.isSame(treeroot1.right, treeroot2.right)