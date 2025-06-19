# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = []
        def traversal(root, path):
            if root is None:
                return

            if root.left is None and root.right is None:
                paths.append(path + [str(root.val)])
                return

            traversal(root.left, path + [str(root.val)])
            traversal(root.right, path + [str(root.val)])
        
        traversal(root, [])

        answer = []
        for p in paths:
            answer.append("->".join(p))

        return answer