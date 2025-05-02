# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layer = defaultdict(list)

        def traversal(root, depth):
            if root is None:
                return
            
            layer[depth].append(root.val)
            traversal(root.right, depth+1)
            traversal(root.left, depth+1)

        traversal(root, 0)

        answer = []
        for k in layer.keys():
            answer.append(layer[k][0])

        return answer