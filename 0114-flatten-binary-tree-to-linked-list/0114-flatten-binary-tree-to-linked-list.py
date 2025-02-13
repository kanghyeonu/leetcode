# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def preorder(r):
            if r is None:
                return
            
            nodes.append(r)

            preorder(r.left)
            preorder(r.right)

        preorder(root)
        for i in range(1, len(nodes)):
            nodes[i-1].right = nodes[i]
            nodes[i-1].left = None