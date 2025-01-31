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
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        curr = slow
        currHead = slow

        while curr.next:
            temp = curr.next
            prev.next = temp
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            temp.next = currHead
            currHead = temp
        
        answer = 0
        currMid = currHead
        currStart = head

        while currMid:
            answer = max(answer, currMid.val + currStart.val)
            currStart = currStart.next
            currMid = currMid.next
        
        return answer

# @lc code=end

