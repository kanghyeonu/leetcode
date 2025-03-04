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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode newHead = new ListNode(0, head);
        ListNode prev = newHead;
        ListNode curr = head;
        int count = 1;

         while (true) {
            ListNode tail = prev;
            for (int i = 0; i < k; i++) {
                tail = tail.next;
                if (tail == null) {
                    return newHead.next;
                }
            }

            ListNode nextGroupHead = tail.next;
            ListNode[] reversedList = reverse(curr, tail);
            prev.next = reversedList[0]; // 새로 뒤집힌 헤드 연결
            reversedList[1].next = nextGroupHead; // 새로 뒤집힌 테일 연결
            
            prev = reversedList[1]; // prev를 업데이트
            curr = nextGroupHead; // curr을 다음 그룹 헤드로 업데이트
        }

    }

    ListNode[] reverse(ListNode head, ListNode tail) {
        ListNode prev = tail.next;
        ListNode curr = head;

        while (prev != tail) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return new ListNode[]{tail, head};
    }
}