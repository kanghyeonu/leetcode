# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def preOrder(r):
            if r is None:
                return
            
            answer.append(r.val)
            preOrder(r.left)
            preOrder(r.right)
        
        preOrder(root)
        return answer