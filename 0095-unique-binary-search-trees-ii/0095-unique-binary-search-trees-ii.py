# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = dict()

        def generate(start, end):
            BSTs = []
            if start > end:
                BSTs.append(None)
                return BSTs
                
            if (start, end) in cache:
                return cache[(start, end)]

            # root i
            for i in range(start, end + 1): 
                leftTree = generate(start, i-1)
                rightTree = generate(i+1, end)

                for l in range(len(leftTree)):
                    for r in range(len(rightTree)):
                        root = TreeNode(i)
                        root.left = leftTree[l]
                        root.right = rightTree[r]

                        BSTs.append(root)

            cache[(start, end)] = BSTs
            return BSTs
        
        return generate(1, n)