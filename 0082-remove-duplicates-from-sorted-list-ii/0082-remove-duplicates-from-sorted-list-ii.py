# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        if head.next == None:
            return head

        prev = ListNode(-101, head)
        tempHead = prev
        dupVal = -101
        curr = head

        while curr.next != None:
            next_ = curr.next
            if curr.val == next_.val:
                dupVal = curr.val
                curr = next_
                prev.next = next_
            elif curr.val == dupVal:
                curr = next_
                prev.next = next_  
            else:
                dupVal = curr.val
                prev = curr
                curr = next_

        if curr.val == dupVal:
            prev.next = curr.next

        return tempHead.next
            
