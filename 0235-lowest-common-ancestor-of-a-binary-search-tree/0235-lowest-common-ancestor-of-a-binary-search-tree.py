# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getNodePath(r, node, path):
            if r is None:
                return None

            path.append(r)

            if r == node:
                return path

            left_path = getNodePath(r.left, node, path)
            if left_path is not None:
                return left_path

            right_path = getNodePath(r.right, node, path)
            if right_path is not None:
                return right_path

            path.pop() 

            return None

        pPath = getNodePath(root, p, [])
        qPath = getNodePath(root, q, [])

        minLen = min(len(pPath), len(qPath))

        for i in range(minLen):
            if pPath[i].val != qPath[i].val:
                return pPath[i-1]
         
            if i == minLen-1:
                return pPath[i]

