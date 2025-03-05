# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(r, sum):
            if r is None:
                return

            sum += str(r.val)
            if r.left is None and r.right is None:
                self.answer += int(sum)
                return

            dfs(r.left, sum)
            dfs(r.right, sum)

        dfs(root, "")

        return self.answer