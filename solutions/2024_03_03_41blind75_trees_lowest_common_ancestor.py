# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# all tests passed
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # if find p and q in left then check left
    # if p and q diff sides, curr is lowest
    # if find p and q in right then check right
    if p.val <= root.val and q.val >= root.val or (p.val >= root.val and q.val <= root.val):
        return root

    elif p.val >= root.val and q.val >= root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    
    else:
        return self.lowestCommonAncestor(root.left, p, q)