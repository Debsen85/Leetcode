#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        cycle = False
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                cycle = True
                break
        if not cycle:
            return -1
        curr = nums[0]
        while curr != slow:
            curr = nums[curr]
            slow = nums[slow]
        return curr
        
# @lc code=end

