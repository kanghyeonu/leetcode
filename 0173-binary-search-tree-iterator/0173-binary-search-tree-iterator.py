# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.nodes = []
        def inOrder(root):
            if root is None:
                return
            
            inOrder(root.left)
            self.nodes.append(root.val)
            inOrder(root.right)
        
        inOrder(root)


    def next(self) -> int:
        if self.idx < len(self.nodes):
            self.idx += 1

        return self.nodes[self.idx - 1]

    def hasNext(self) -> bool:
        if self.idx < len(self.nodes):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()