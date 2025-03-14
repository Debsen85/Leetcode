#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        Rows = len(matrix)
        Cols = len(matrix[0])

        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in range(Rows):
            for c in range(Cols):
                if r in rows or c in cols:
                    matrix[r][c] = 0
        
# @lc code=end

