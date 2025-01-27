# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def traversal(r, depth):
            if r is None:
                return
            
            if len(answer) <= depth:
                answer.append([])
            
            answer[depth].append(r.val)

            traversal(r.left, depth + 1)
            traversal(r.right, depth + 1)
        
        traversal(root, 0)

        return answer