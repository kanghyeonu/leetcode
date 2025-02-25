# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(r):
            if r is None:
                return 0

            
            leftSum = dfs(r.left)
            rightSum = dfs(r.right)
            # 전체 최대 합 계산
            rootSum = leftSum + rightSum + r.val
            # 부분 최대 합 계산(pathSum 값)
            maxSum = max(leftSum + r.val, rightSum + r.val, r.val)
            
            self.answer = max(maxSum, rootSum, self.answer)

            return maxSum

        dfs(root)

        return self.answer