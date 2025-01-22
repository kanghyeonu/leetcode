# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        values = []
        nodes = []
        def traversal(r):
            if r is None:
                return
            
            traversal(r.left)
            values.append(r.val)
            nodes.append(r)
            traversal(r.right)
        
        traversal(root)

        values.sort()
        for i in range(len(values)):
            nodes[i].val = values[i]
            
