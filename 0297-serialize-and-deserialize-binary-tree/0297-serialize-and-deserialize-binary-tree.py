# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encoded = []
        def traversal(r):
            if r is None:
                encoded.append("n")
                return
            
            encoded.append(str(r.val))
            traversal(r.left)
            traversal(r.right)
        
        traversal(root)

        return ",".join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(","))  

        def build():
            val = next(values)
            if val == "n":
                return None

            node = TreeNode(int(val))

            node.left = build()
            node.right = build()
            
            return node

        return build()

            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))