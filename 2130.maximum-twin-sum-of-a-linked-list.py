#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = slow
        mid = slow.next
        curr = mid

        while curr.next:
            temp = curr.next
            curr.next = temp.next
            prev.next = temp
            temp.next = mid
            mid = temp
        
        answer = 0

        front = head

        while mid:
            answer = max(answer, front.val + mid.val)
            front = front.next
            mid = mid.next

        return answer

# @lc code=end

