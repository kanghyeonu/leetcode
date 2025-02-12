# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        def getPathSum(r, elements):
            if r is None: 
                return 

            elements = elements + [r.val]
            if r.left is None and r.right is None and sum(elements) == targetSum:
                answer.append(elements)
                return

            getPathSum(r.left, elements)
            getPathSum(r.right, elements)

        getPathSum(root, [])

        return answer
