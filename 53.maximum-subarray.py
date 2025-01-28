#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        total = nums[0]
        for i in range(len(nums)):
            if currSum <= 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            total = max(total, currSum)
        return total 
        
# @lc code=end

