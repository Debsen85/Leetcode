#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(min(len(mat1[0]), len(mat2[0])))] for _ in range(len(mat1))]
        hashMap1, hashMap2 = {}, {}
        for r in range(len(mat1)):
            for c in range(len(mat1[0])):
                hashMap1[(r, c)] = mat1[r][c]
        for r in range(len(mat2)):
            for c in range(len(mat2[0])):
                hashMap2[(r, c)] = mat2[r][c]
        for r in range(len(mat1)):
            for c in range(min(len(mat1[0]), len(mat2[0]))):
                total = 0
                for d in range(len(mat2)):
                    total += (mat1[r][d] * mat2[d][c])
                result[r][c] = total
        return result
        
# @lc code=end

