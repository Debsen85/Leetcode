#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col, answer = len(grid), len(grid[0]), 0
        mapRow, mapCol = defaultdict(int), defaultdict(int)
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    mapRow[r] += 1
        for c in range(col):
            for r in range(row):
                if grid[r][c]:
                    mapCol[c] += 1
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    if mapRow[r] > 1 or mapCol[c] > 1:
                        answer += 1
        return answer
# @lc code=end

