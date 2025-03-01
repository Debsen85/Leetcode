#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row = [0] * n
        col = [0] * n

        for i in range(n):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])

        for i in range(n):
            for j in range(n):
                col[i] = max(col[i], grid[j][i])

        
        answer = 0

        for i in range(n):
            for j in range(n):
                value = min(row[i], col[j])
                if value > grid[i][j]:
                    answer += value - grid[i][j]

        return answer
# @lc code=end

