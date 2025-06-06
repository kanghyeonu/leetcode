# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def traversal(r):
            if r is None:
                return
            
            values.append(r.val)

            traversal(r.left)
            traversal(r.right)

        traversal(root)
        values.sort()

        return values[k-1]