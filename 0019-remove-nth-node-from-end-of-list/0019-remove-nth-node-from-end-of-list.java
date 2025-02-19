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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null){
            return null;
        }
        ListNode curr = head;
        ListNode prev;
        int count = 0;
        while (curr != null){
            count ++;
            prev = curr;
            curr = curr.next;
        }
        
        ListNode tempHead = new ListNode(0, head);
        curr = head;
        prev = tempHead;
        int target = count - n;
        count = 0;
        while (curr != null){
            if (count == target){
                prev.next = curr.next;
                break;
            }
            count++;
            prev = curr;
            curr = curr.next;
        }
        return tempHead.next;
        
    }
}