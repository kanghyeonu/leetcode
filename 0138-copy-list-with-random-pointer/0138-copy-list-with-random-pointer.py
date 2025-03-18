"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        mapping = dict()
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            newNode = mapping[curr]
            if curr.next:
                newNode.next = mapping[curr.next]
            if curr.random:
                newNode.random = mapping[curr.random]

            curr = curr.next

        return mapping[head]
