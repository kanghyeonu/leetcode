# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(lst):
            if not lst:
                return None

            m = len(lst)//2
            root = TreeNode(lst[m])

            root.left = build(lst[:m])
            root.right = build(lst[m+1:])

            return root

        return build(nums)