# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode(None, None)
        head = answer

        while 1:
            Min = float('inf')
            index = -1
            for i, current in enumerate(lists):
                if current is None:
                    continue
                
                if Min > current.val:
                    Min = current.val
                    index = i

                if answer.val == Min:
                    break

            if index == -1:
                break

            answer.next = ListNode(Min)
            lists[index] = lists[index].next
            answer = answer.next


        return head.next