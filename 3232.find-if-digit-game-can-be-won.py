#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1, sum2 = 0, 0
        for num in nums:
            if num < 10:
                sum1 += num
            else:
                sum2 += num
        return sum1 != sum2 
        
# @lc code=end

