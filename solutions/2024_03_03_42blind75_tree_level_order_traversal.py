# https://leetcode.com/problems/binary-tree-level-order-traversal/
# all tests passed
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:

    if not root:
        return []
    output = []
    q = deque()
    q.append(root)
    while q:
        num_nodes = len(q)
        tempout = []
        while num_nodes > 0:
            curr = q.popleft()
            num_nodes -=1
            tempout.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            
        output.append(tempout)

    return output