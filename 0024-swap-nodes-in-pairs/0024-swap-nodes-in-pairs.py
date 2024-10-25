# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        current = head
        previous= None
        flag = True
        
        while current != None:
            if current.next == None:
                break

            swap1 = current
            swap2 = current.next
            current = swap2.next
            if previous != None:
                previous.next = swap2
            previous = swap1
            if flag:
                answer = swap2
                flag = False

            swap1.next = swap2.next
            swap2.next = swap1

        

        return answer