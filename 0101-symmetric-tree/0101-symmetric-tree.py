# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traversal(l, r):
            if l is None and r is None:
                return True
            # xor
            if (l is None and not r is None) or (not l is None and r is None):
                return False
            
            if l.val != r.val:
                return False
            
            return traversal(l.left, r.right) and  traversal(l.right, r.left)

        return traversal(root.left, root.right)