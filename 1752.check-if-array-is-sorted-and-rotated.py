#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        decreasingPoint = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                decreasingPoint += 1
                if decreasingPoint > 1:
                    return False
        if decreasingPoint == 0:
            return True
        return True if nums[-1] <= nums[0] else False
        
# @lc code=end

