# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        
        lessNodes = ListNode(0, None)
        lessCurr = lessNodes

        greaterNodes = ListNode(0, None)
        greaterCurr = greaterNodes

        while curr != None:
            if curr.val < x:
                lessCurr.next = curr
                lessCurr = lessCurr.next
            else:
                greaterCurr.next = curr
                greaterCurr = greaterCurr.next

            curr = curr.next

        lessCurr.next = greaterNodes.next
        greaterCurr.next = None

        return lessNodes.next