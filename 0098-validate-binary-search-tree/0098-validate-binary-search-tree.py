# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traversal(r, low, high):
            if r is None:
                return True

            if not (low < r.val < high):
                return False
             
            return  (traversal(r.left, low, r.val)) and (traversal(r.right, r.val, high))
        
        return traversal(root, float('-inf'), float('inf'))

    
