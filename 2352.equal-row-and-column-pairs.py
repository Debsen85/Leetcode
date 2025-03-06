#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashSet = defaultdict(int)
        row, col = len(grid), len(grid[0])

        for i in range(row):
            hashSet[tuple(grid[i])] += 1

        answer = 0

        for i in range(col):
            column = []
            for j in range(row):
                column.append(grid[j][i])
            if tuple(column) in hashSet:
                answer += hashSet[tuple(column)]
            
        return answer

# @lc code=end

