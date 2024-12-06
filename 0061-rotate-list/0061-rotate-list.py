# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        l = 1
        start = head
        while start.next != None:
            start = start.next
            l += 1
        lastNode = start

        k = k % l
        if k == 0:
            return head
            
        newTail_index, p = l-k-1, 0
        newTail = head
        while p < newTail_index:
            newTail = newTail.next
            p += 1

        newHead = newTail.next
        newTail.next = None
        lastNode.next = head
        head = newHead

        return head