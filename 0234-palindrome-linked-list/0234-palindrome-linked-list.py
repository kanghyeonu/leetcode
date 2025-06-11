# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        if len(values) % 2 == 0:
            m = len(values) // 2
            return True if values[:m] == values[m:][::-1] else False
        
        else:
            m = len(values) // 2 + 1
            return True if values[:m-1] == values[m:][::-1] else False