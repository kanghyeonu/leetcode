# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        b = set()
        
        currA = headA
        currB = headB
        while currA is not None or currB is not None:
            if currA is not None:
                if currA in b:
                    return currA
                
                a.add(currA)
                currA = currA.next
                
            if currB is not None:
                if currB in a:
                    return currB
            
                b.add(currB)
                currB = currB.next
                
        return None