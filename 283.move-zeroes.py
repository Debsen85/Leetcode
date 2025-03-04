#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums) and i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
# @lc code=end

