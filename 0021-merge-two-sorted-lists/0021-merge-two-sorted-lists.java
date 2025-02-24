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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode curr1 = list1;
        ListNode curr2 = list2;
        ListNode answerHead = new ListNode(0, null);
        ListNode answerCurr = answerHead;
        while (curr1 != null || curr2 != null){
            if (curr1 == null){
                answerCurr.next = curr2;
                curr2 = curr2.next;
                answerCurr = answerCurr.next;
                continue;
            }
            if (curr2 == null){
                answerCurr.next = curr1;
                curr1 = curr1.next;
                answerCurr = answerCurr.next;
                continue;
            }

            if (curr1.val > curr2.val){
                answerCurr.next = curr2;
                curr2 = curr2.next;    
            } 
            else {
                answerCurr.next = curr1;
                curr1 = curr1.next;    
            }
            answerCurr = answerCurr.next;
        }

        return answerHead.next;
    }
}