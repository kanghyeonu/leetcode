/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode newHead = new ListNode(0, head);
        ListNode prev = newHead;
        ListNode curr = head;

        while (curr != null && curr.next != null){
            ListNode swap1 = curr;
            ListNode swap2 = curr.next;

            curr = swap2.next;
            swap2.next = swap1;
            swap1.next = curr;

            prev.next = swap2;
            prev = swap1;
        }
        
        return newHead.next;
    }

}