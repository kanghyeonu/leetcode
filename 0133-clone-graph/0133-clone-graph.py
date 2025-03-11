"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        graph = dict()
        visited = set()

        dq = deque([node])
        visited.add(node)

        while dq:
            n = dq.popleft()

            if n.val not in graph:
                graph[n.val] = Node(n.val)

            for adj in n.neighbors:
                if adj not in visited:
                    visited.add(adj)
                    dq.append(adj)

                if adj.val not in graph:
                    graph[adj.val] = Node(adj.val)
                    
                graph[n.val].neighbors.append(graph[adj.val])

        return graph[node.val]

        
        