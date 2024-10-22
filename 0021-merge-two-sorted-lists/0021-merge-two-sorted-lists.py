# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
            
        current1 = list1
        current2 = list2
        answer = ListNode()
        temp = answer
        while current1 != None or current2 != None:
            temp.next = ListNode()
            temp = temp.next
            if current1 is None:
                temp.val = current2.val
                current2 = current2.next            
                continue
            elif current2 is None:
                temp.val = current1.val
                current1 = current1.next
                continue
            
            if current1.val < current2.val:
                temp.val = current1.val
                current1 = current1.next
            else:
                temp.val = current2.val
                current2 = current2.next
        
        return answer.next
                