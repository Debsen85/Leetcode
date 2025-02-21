#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr1, curr2, curr3 = list1, list2, dummy
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
        
        while curr1:
            curr3.next = curr1
            curr1 = curr1.next
            curr3 = curr3.next
        
        while curr2:
            curr3.next = curr2
            curr2 = curr2.next
            curr3 = curr3.next
        
        return dummy.next
# @lc code=end

