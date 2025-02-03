#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        parity = 0
        length = 1
        maxLength = 1
        if nums[1] > nums[0]:
            length = 2
            parity = 1
        elif nums[1] < nums[0]:
            length = 2
            parity = -1
        else:
            length = 1
            parity = 0
        maxLength = max(maxLength, length)
        index = 2
        while index < len(nums):
            if nums[index] > nums[index - 1]:
                if parity == 1:
                    length += 1
                else:
                    length = 2
                    parity = 1
            elif nums[index] < nums[index - 1]:
                if parity == -1:
                    length += 1
                else:
                    length = 2
                    parity = -1
            else:
                length = 1
                parity = 0
            maxLength = max(maxLength, length)
            index += 1
        return maxLength
        
# @lc code=end

