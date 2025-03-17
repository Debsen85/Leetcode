#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = {}
        
        def backtrack(i, j):
            if j == row:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            result = triangle[j][i] + min(backtrack(i + 1, j + 1), backtrack(i, j + 1))
            dp[(i, j)] = result
            return result
        return backtrack(0, 0)
# @lc code=end

