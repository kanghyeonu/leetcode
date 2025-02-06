# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height_differ(r):
            if r is None:
                return  0
            
            left_h = get_height_differ(r.left)
            right_h = get_height_differ(r.right)

            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1

            return 1 + max(left_h, right_h)

    
        return get_height_differ(root) != -1
        