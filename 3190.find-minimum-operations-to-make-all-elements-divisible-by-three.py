#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = 0
        for num in nums:
            if num % 3: d += 1
        return d
# @lc code=end

