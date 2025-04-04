# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nodes = []
        curr = head
        while curr != None:
            nodes.append(curr)
            curr = curr.next
        
        nodes.sort(key=lambda x: x.val)

        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
        nodes[-1].next = None
        
        return nodes[0]