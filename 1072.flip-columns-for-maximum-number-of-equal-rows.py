#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
from typing import List

class Solution:
    def flip(self, arr):
        for i in range(len(arr)):
            if arr[i]:
                arr[i] = 0
            else:
                arr[i] = 1
        return arr

    def string(self, arr):
        value = ""
        for a in arr:
            value += str(a)
        return value

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        bitMap = {}

        for mat in matrix:
            a = self.string(mat)
            b = self.string(self.flip(mat))

            bitMap[a] = bitMap.get(a, 0) + 1
            bitMap[b] = bitMap.get(b, 0) + 1
        
        return max(bitMap.values())
        
# @lc code=end

