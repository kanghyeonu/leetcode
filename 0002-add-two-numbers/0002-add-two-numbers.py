# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        answer_current = answer
        carry = 0

        while 1:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            sum_val = (l1_val + l2_val + carry)
            answer_current.val = sum_val%10
            carry = sum_val//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if l1 or l2 or carry:
                answer_current.next = ListNode(0)
                answer_current = answer_current.next
            else:
                break
            
        return answer
            