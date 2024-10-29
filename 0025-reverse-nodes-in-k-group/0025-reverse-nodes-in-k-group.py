# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
     
        answer = ListNode()
        answer.next = head
        
        current = head
        tail = answer
        l = [current]
        while current.next is not None:
            current = current.next
            next_ = current.next
            l.append(current)
            if len(l) == k:
                for i in range(k-1):
                    l[(-1)*i - 1].next = l[(-1)*i - 2]
                l[0].next = next_
                tail.next = l[-1]
                tail = l[0]
                current = tail
                l.clear()
                

        return answer.next
            

                
           





