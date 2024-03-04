# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# all tests passed
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    # root is at the beginning of preorder list
    # root is in the mid of inorder list
    if not preorder or not inorder:
        return None


    curr = TreeNode(preorder[0])
    rootidx = inorder.index(preorder[0])
    

    curr.left = self.buildTree(preorder[1:rootidx+1], inorder[:rootidx])
    curr.right = self.buildTree(preorder[rootidx+1:], inorder[rootidx+1:])

    return curr