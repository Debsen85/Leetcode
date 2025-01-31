#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        
        for i in range(len(nums)):
            if i == 0:
                if nums[-1] - nums[i] == 0:
                    return i
            elif i == len(nums) - 1:
                if nums[i - 1] == 0:
                    return i
            else:
                if nums[-1] - nums[i] == nums[i - 1]:
                    return i
        return -1
# @lc code=end

