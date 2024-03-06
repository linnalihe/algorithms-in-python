# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# all tests passed
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = [root.val]
        self.helper(root, max_sum)

        return max_sum[0]

    def helper(self, root, max_sum):

        if not root:
            return 0

        sum_left = self.helper(root.left, max_sum)
        sum_right = self.helper(root.right, max_sum)

        max_sum[0] = max(max_sum[0], root.val + sum_left + sum_right, root.val+max(sum_left, sum_right, 0))
        return root.val+max(sum_left, sum_right, 0)

        