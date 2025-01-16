# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def Traversal(r):
            if r == None:
                return
        
            Traversal(r.left)
            answer.append(r.val)
            Traversal(r.right)
        
        Traversal(root)
        
        return answer