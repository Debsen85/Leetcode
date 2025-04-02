#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start
from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        points = []
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    points.append((i, j))
        
        x = sorted([X[1] for X in points])
        y = sorted([Y[0] for Y in points])

        targetY = x[len(x) // 2]
        targetX = y[len(y) // 2]

        answer = 0

        for i, j in points:
            answer += abs(i - targetX) + abs(j - targetY)

        return answer
# @lc code=end

