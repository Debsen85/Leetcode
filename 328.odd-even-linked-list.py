#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                odd = head
                even = head.next

                dummy = head.next

                while even and even.next:
                    odd.next = even.next
                    odd = odd.next

                    even.next = odd.next
                    even = even.next

                odd.next = dummy
                
            return head
        
        return None
# @lc code=end

