# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        path = set()

        while curr:
            if curr not in path:
                path.add(curr)
            else:
                return curr

            curr = curr.next

        return None
            

            