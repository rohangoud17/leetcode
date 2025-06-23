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
    public ListNode removeElements(ListNode head, int val) {
        ListNode temp = new ListNode(0, head);
        ListNode newNode = temp;

        while(newNode != null){
            while(newNode.next != null && newNode.next.val == val){
                newNode.next = newNode.next.next;
            }
            newNode = newNode.next;
        }
        return temp.next;
    }
}