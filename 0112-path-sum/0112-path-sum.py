# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def getPathSum(r, pathSum):
            if r.left is None and r.right is None and pathSum + r.val == targetSum:
                return True

            leftResult = getPathSum(r.left, r.val+pathSum) if r.left is not None else False
            rightResult = getPathSum(r.right, r.val+pathSum) if r.right is not None else False

            return leftResult or rightResult

        return getPathSum(root, 0)

