# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def traversal(r, depth):
            if r is None:
                return
            
            if depth >= len(answer):
                answer.append([])
            
            answer[depth].append(r.val)

            traversal(r.left, depth + 1)
            traversal(r.right, depth + 1)

        traversal(root, 0)

        for i in range(len(answer)):
            if i%2 == 1:
                answer[i] = answer[i][::-1]

        return answer