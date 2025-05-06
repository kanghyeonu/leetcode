# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tempHead = ListNode(0, head)
        currNode = tempHead
        while currNode.next is not None:
            nextNode = currNode.next
            if val == nextNode.val:
                nextNode = nextNode.next
                currNode.next = nextNode
            else:
                currNode = currNode.next

        return tempHead.next