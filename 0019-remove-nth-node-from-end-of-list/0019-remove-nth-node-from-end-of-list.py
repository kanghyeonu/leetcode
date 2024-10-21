# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        sz = 1
        while current.next != None: 
            current = current.next
            sz += 1

        if sz == 1:
            return None
        elif sz == n:
            return head.next
            
        target = sz
        current = head
        while target-1 > n:
            current = current.next
            target -= 1

        removed = current.next
        current.next = removed.next

        return head
