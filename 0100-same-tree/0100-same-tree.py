# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversal(pr, qr):
            if pr is None and qr is None:
                return True
            # xor
            if (pr is None and not qr is None) or (not pr is None and qr is None):
                return False

            if pr.val != qr.val:
                return False
            
            return traversal(pr.left, qr.left) and traversal(pr.right, qr.right)
    
        return traversal(p, q)
