# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postOrder(r):
            if r is None:
                return
            
            postOrder(r.left)
            postOrder(r.right)
            answer.append(r.val)

        postOrder(root)
        return answer
        