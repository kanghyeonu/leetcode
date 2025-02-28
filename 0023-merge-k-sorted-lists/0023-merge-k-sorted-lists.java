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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0){
            return null;
        }
        int len = lists.length;

        ListNode answer = new ListNode(-1000000, null);
        ListNode answerHead = answer;

        int minIndex = 0;
        int minVal = 100000;
        while (!isNull(lists)){
            for (int i = 0; i < len; i++){
                ListNode node = lists[i];
                if (node == null){
                    continue;     
                }

                if (answer.val == node.val){
                    minVal = node.val;
                    minIndex = i;
                    break;
                }

                if (minVal > node.val){
                    minVal = node.val;
                    minIndex = i;
                }
            }
            lists[minIndex] = lists[minIndex].next;

            ListNode newNode = new ListNode(minVal);
            answer.next = newNode;
            answer = newNode;
            minVal = 100000;
        }

        return answerHead.next;
    }

    boolean isNull(ListNode[] lists){
        int len = lists.length;
        for (int i = 0; i < len; i++){
            if (lists[i] != null){
                return false;
            }
        }
        return true;
    }
}