/*
 * @lc app=leetcode id=143 lang=java
 *
 * [143] Reorder List
 */

// @lc code=start
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
    public void reorderList(ListNode head) {
        if (head.next != null) {

            if (head.next.next != null) {

                ListNode slow = head;
                ListNode fast = head;

                while(fast != null && fast.next != null) {
                    slow = slow.next;
                    fast = fast.next.next;
                }

                ListNode reverse = slow.next;
                ListNode currHead = slow.next;

                while (reverse.next != null) {
                    ListNode temporary = reverse.next;

                    if (reverse.next.next != null) {
                        reverse.next = reverse.next.next;
                    } else {
                        reverse.next = null;
                    }

                    slow.next = temporary;
                    temporary.next = currHead;
                    currHead = temporary;
                }
                slow = head;
                fast = head;

                while(fast != null && fast.next != null) {
                    slow = slow.next;
                    fast = fast.next.next;
                }

                ListNode curr = head;

                while (slow.next != null) {
                    ListNode temporary = slow.next;

                    if (slow.next.next != null) {
                        slow.next = slow.next.next;
                    } else {
                        slow.next = null;
                    }
                    
                    temporary.next = curr.next;
                    curr.next = temporary;
                    curr = curr.next.next;
                }
            }
        }
    }
}
// @lc code=end

