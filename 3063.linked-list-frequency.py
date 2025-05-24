#
# @lc app=leetcode id=3063 lang=python3
#
# [3063] Linked List Frequency
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = {}
        curr = head
        while curr:
            if curr.val not in answer:
                answer[curr.val] = 1
            else:
                answer[curr.val] += 1
            curr = curr.next
        dummy = ListNode(0)
        curr = dummy
        for val in list(answer.values()):
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
# @lc code=end

