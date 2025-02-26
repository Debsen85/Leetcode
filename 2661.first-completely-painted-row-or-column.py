#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#

# @lc code=start
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        arrayMap = {}
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                arrayMap[mat[r][c]] = (r, c)

        row = [0] * rows
        col = [0] * cols

        for i, ar in enumerate(arr):
            r, c = arrayMap[ar]

            row[r] += 1
            col[c] += 1
        
            if row[r] == cols or col[c] == rows:
                return i
                
        return -1
# @lc code=end

