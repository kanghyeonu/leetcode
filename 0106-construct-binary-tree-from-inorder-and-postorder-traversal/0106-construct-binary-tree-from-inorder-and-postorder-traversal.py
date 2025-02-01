# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build(postOrder, inOrder):
            if not inOrder or not postOrder:
                return None
            
            rootVal = postOrder.pop()
            root = TreeNode(rootVal)

            subTreeIdx = inOrder.index(rootVal)

            root.right = build(postOrder, inOrder[subTreeIdx+1:])
            root.left = build(postOrder, inOrder[:subTreeIdx])

            return root
        
        return build(postorder, inorder)