# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preOrder, inOrder):
            if not preOrder or not inOrder:
                return None

            rootVal = preOrder.pop(0)
            root = TreeNode(rootVal)

            subTreeIdx = inOrder.index(rootVal)

            root.left = build(preOrder, inOrder[:subTreeIdx])
            root.right = build(preOrder, inOrder[subTreeIdx+1:])

            return root

        return build(preorder, inorder)