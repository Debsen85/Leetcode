#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                cycle = True
                break
        if not cycle:
            return None
        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next
        return curr

        
# @lc code=end

