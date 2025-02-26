#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = -(10 ** 9)
        minSum = 10 ** 9
        
        currSum = 0

        for num in nums:
            if currSum <= 0:
                currSum = num
            else:
                currSum += num
            
            maxSum = max(currSum, maxSum)
        
        currSum = 0

        for num in nums:
            if currSum >= 0:
                currSum = num
            else:
                currSum += num
            
            minSum = min(currSum, minSum)
        
        return max(maxSum, abs(minSum))

# @lc code=end

