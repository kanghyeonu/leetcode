# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(-101, head)
        prev = tempHead
        curr = head

        while curr is not None:
            next_ = curr.next
            if next_ is not None and next_.val == curr.val:
                prev.next = next_
                curr = next_
            else:
                prev = curr
                curr = next_ 
                    
        return tempHead.next