# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traversal(r, depth):
            if r is None:
                return
            
            self.answer = max(depth, self.answer)

            traversal(r.left, depth + 1)
            traversal(r.right, depth + 1)
        
        traversal(root, 1)

        return self.answer