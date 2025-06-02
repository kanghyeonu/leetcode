# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if root is None:
                return None
            
            leftSide = invert(root.left)
            rightSide = invert(root.right)
            
            root.left = rightSide
            root.right = leftSide
            return root
        
        answer = invert(root)

        return answer
