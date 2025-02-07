# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_d = float("inf")
        def getDepth(r, depth):
            nonlocal min_d
            if r is None:
                return 
            if min_d <= depth:
                return
            if not r.left and not r.right:
                min_d = min(min_d, depth)
            
            getDepth(r.left, depth+1)
            getDepth(r.right, depth+1)

        getDepth(root, 1)
        return min_d

            
