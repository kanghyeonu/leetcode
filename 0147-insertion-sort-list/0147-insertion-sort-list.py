# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedListHead = ListNode(float("-inf"))
        curr = head

        while curr != None:
            prev = sortedListHead

            while prev.next != None and prev.next.val < curr.val:
                prev = prev.next
            
            next = curr.next

            # 정렬 리스트에 넣기
            curr.next = prev.next
            prev.next = curr

            curr = next
        
        return sortedListHead.next
    
    