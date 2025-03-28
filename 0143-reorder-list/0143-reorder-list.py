# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        #  6 [0..5]
        # 0 5 1 4 2 3
        #  3 [0..2]
        # 0 2 1 
        
        start = 1
        end = len(nodes) - 1
        curr = head
        while start <= end:
            if start == end:
                curr.next = nodes[start]
                curr = curr.next
                curr.next = None
                return

            n1 = nodes[start]
            n2 = nodes[end]

            n2.next = n1
            curr.next = n2
            curr = n1
            curr.next = None

            start += 1
            end -= 1
        