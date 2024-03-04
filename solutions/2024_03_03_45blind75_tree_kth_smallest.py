# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# all tests passed
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    # bruteforce is to put everything in an array, in sorted order
    # better do a dfs
    count = 0
    curr = root
    s = [curr]
    while s:
        while curr:
            s.append(curr)
            curr = curr.left

        curr = s.pop()
        count+=1
            
        if count == k:
            return curr.val
        
        curr = curr.right