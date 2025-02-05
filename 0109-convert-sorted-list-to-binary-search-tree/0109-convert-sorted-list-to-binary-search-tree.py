# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    
        def build(lst):
            if not lst:
                return None

            m = len(lst) // 2
            root = TreeNode(lst[m])

            root.left = build(lst[:m])
            root.right = build(lst[m+1:])
            return root

        values = []
        curr = head
        while curr != None:
            values.append(curr.val)
            curr = curr.next
        
        return build(values)