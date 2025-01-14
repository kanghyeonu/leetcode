# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        tempHead = ListNode(0, head)
        index = 0
        curr = tempHead
        startPoint, endPoint = None, None
        reverseHead, reverseTail = None, None

        while curr != None and index <= right + 1:
            if index == left - 1:
                startPoint = curr
            elif index == left:
                reverseHead = curr
            elif index == right:
                reverseTail = curr
            elif index == right + 1:
                endPoint = curr

            curr = curr.next
            index += 1

        startPoint.next, reverseTail.next = None, None

        reverseListHead = ListNode(0, None)
        reverseListCurr = reverseListHead
        curr = reverseHead

        while curr != None:
            next_ = curr.next
            reverseListHead.next = curr
            curr.next = reverseListCurr
            reverseListCurr = curr
            curr = next_
        
        startPoint.next, reverseHead.next = reverseListHead.next, endPoint
        return tempHead.next

        



        




        