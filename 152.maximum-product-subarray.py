#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMax, currMin = 1, 1
        for num in nums:
            if num == 0:
                currMax, currMin = 1, 1
                continue
            temp = num * currMax
            currMax = max(temp, num * currMin, num)
            currMin = min(temp, num * currMin, num)

            result = max(result, currMin, currMax)
        return result
# @lc code=end

