"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        nodes = defaultdict(list)
        def traversal(r, depth):
            if r is None:
                return
            
            nodes[depth].append(r)

            traversal(r.left, depth+1)
            traversal(r.right, depth+1)
            return
        
        traversal(root, 0)

        for d, ns in nodes.items():
            for i in range(len(ns)-1):
                ns[i].next = ns[i+1]
        
        return root