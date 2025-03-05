#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        maxAverage = float('-inf')
        total = 0

        while j < len(nums):
            total += nums[j]

            if j - i + 1 > k:
                total -= nums[i]
                i += 1

            if j - i + 1 == k:
                maxAverage = max(maxAverage, total)
            
            j += 1
        return maxAverage / k
        
# @lc code=end

