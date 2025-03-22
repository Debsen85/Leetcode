#
# @lc app=leetcode id=2679 lang=python3
#
# [2679] Sum in a Matrix
#

# @lc code=start
from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total = 0
        r, c = len(nums), len(nums[0])
        for i in range(r):
            nums[i].sort()

        for j in range(c):
            m = 0
            for i in range(r):
                m = max(m, nums[i][j])
            total += m
            
        return total
        
# @lc code=end

