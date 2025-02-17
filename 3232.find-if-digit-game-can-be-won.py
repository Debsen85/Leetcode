#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumTotal = 0
        sumSingle = 0
        for num in nums:
            if num < 10:
                sumSingle += num
            sumTotal += num
        return False if (sumSingle == sumTotal - sumSingle) else True 
        
# @lc code=end

